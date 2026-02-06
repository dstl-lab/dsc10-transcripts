"""Reads objects.parquet and builds database.db using the schema from models.py."""

import json
import sys
import uuid
from datetime import datetime

import pandas as pd
from sqlmodel import Session, SQLModel, create_engine

from dsc10_transcripts.models import Assignment, Conversation, Message, MessageRole


def main():
    db_name = sys.argv[1] if len(sys.argv) > 1 else "database.db"
    df = pd.read_parquet("objects.parquet")

    # Parse object_data JSON for each type
    def get_objects(object_type: str) -> list[dict]:
        rows = df[df["object_type"] == object_type]
        return [json.loads(r) for r in rows["object_data"]]

    assignments_data = get_objects("Assignment")
    interactions_data = get_objects("Interaction")
    students_data = {s["id"]: s for s in get_objects("Student")}

    # Build database
    engine = create_engine(f"sqlite:///{db_name}")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # Insert assignments
        for a in assignments_data:
            session.add(
                Assignment(
                    id=a["id"],
                    course_id=a["course_id"],
                    generated_at=_parse_dt(a.get("assignment_created_at")),
                )
            )

        # Group interactions into conversations by (student_id, question_id, assignment_id)
        idf = pd.DataFrame(interactions_data)
        idf["interaction_timestamp"] = pd.to_datetime(idf["interaction_timestamp"])
        grouped = idf.groupby(["student_id", "question_id", "assignment_id"])

        for (student_id, question_id, assignment_id), group in grouped:
            group = group.sort_values("interaction_timestamp")

            student = students_data.get(student_id, {})
            first_name = student.get("student_first_name", "")
            last_name = student.get("student_last_name", "")
            student_name = f"{first_name} {last_name}".strip() or "Unknown"
            student_email = student.get("student_email_address", "")

            conversation_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{student_id}:{question_id}:{assignment_id}"))

            session.add(
                Conversation(
                    id=conversation_id,
                    assignment_id=assignment_id,
                    question_id=question_id,
                    student_name=student_name,
                    student_email=student_email,
                    started_at=group["interaction_timestamp"].iloc[0],
                    message_count=len(group),
                )
            )

            for _, row in group.iterrows():
                role = (
                    MessageRole.STUDENT
                    if row["interaction_respondent_type"] == "student"
                    else MessageRole.AI_TUTOR
                )
                session.add(
                    Message(
                        conversation_id=conversation_id,
                        role=role,
                        content=row["interaction_text"],
                        timestamp=row["interaction_timestamp"],
                    )
                )

        # Update assignment counts
        for a in assignments_data:
            convos = session.exec(
                Conversation.__table__.select().where(Conversation.assignment_id == a["id"])
            ).all()
            assignment = session.get(Assignment, a["id"])
            assignment.total_conversations = len(convos)
            assignment.total_interactions = sum(c.message_count for c in convos)

        session.commit()

        # Summary
        from sqlmodel import select, func
        a_count = session.exec(select(func.count()).select_from(Assignment)).one()
        c_count = session.exec(select(func.count()).select_from(Conversation)).one()
        m_count = session.exec(select(func.count()).select_from(Message)).one()
        print(f"Created {db_name}: {a_count} assignments, {c_count} conversations, {m_count} messages")


def _parse_dt(val: str | None) -> datetime | None:
    if val is None:
        return None
    return datetime.fromisoformat(val.replace("Z", "+00:00"))


if __name__ == "__main__":
    main()
