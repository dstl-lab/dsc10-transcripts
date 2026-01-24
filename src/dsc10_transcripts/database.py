import re
from datetime import datetime
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine, select

from .models import Assignment, Conversation, Message, MessageRole

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def parse_transcript(file_path: str) -> tuple[dict, list[dict]]:
    """Parse the transcript file and return assignment info and conversations."""
    content = Path(file_path).read_text()

    # Parse header
    assignment = {}
    if match := re.search(r"Generated: (.+)", content):
        assignment["generated_at"] = datetime.strptime(
            match.group(1), "%Y-%m-%d %H:%M:%S"
        )
    if match := re.search(r"Course ID: (.+)", content):
        assignment["course_id"] = match.group(1).strip()
    if match := re.search(r"Assignment ID: (.+)", content):
        assignment["id"] = match.group(1).strip()
    if match := re.search(r"Total Interactions: (\d+)", content):
        assignment["total_interactions"] = int(match.group(1))
    if match := re.search(r"Total Conversations: (\d+)", content):
        assignment["total_conversations"] = int(match.group(1))

    # Split into blocks by dashes - header and messages are separate blocks
    # Format: [header_block][---][conv1_header][---][conv1_messages][---][conv2_header][---]...
    blocks = re.split(r"-{80}", content)[1:]  # Skip header block
    conversations = []

    # Pair up blocks: odd indices are conv headers, even indices are messages
    i = 0
    while i < len(blocks) - 1:
        header_block = blocks[i]
        messages_block = blocks[i + 1] if i + 1 < len(blocks) else ""
        block = header_block + messages_block
        i += 2

        if not block.strip():
            continue

        conv = {"messages": []}

        # Parse conversation metadata
        if match := re.search(r"CONVERSATION ID: (.+)", block):
            conv["id"] = match.group(1).strip()
        if match := re.search(r"Student: (.+?) \((.+?)\)", block):
            conv["student_name"] = match.group(1).strip()
            conv["student_email"] = match.group(2).strip()
        if match := re.search(r"Question ID: (.+)", block):
            conv["question_id"] = match.group(1).strip()
        if match := re.search(r"Started: (.+)", block):
            conv["started_at"] = datetime.strptime(
                match.group(1).strip(), "%Y-%m-%d %H:%M:%S"
            )
        if match := re.search(r"Messages: (\d+)", block):
            conv["message_count"] = int(match.group(1))

        # Parse messages - find all [timestamp] ROLE: patterns
        message_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (STUDENT|AI TUTOR):\n(.*?)(?=\n\n\[|\n\n-{80}|\n\n={80}|\Z)"
        for match in re.finditer(message_pattern, block, re.DOTALL):
            timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
            role = (
                MessageRole.AI_TUTOR
                if match.group(2) == "AI TUTOR"
                else MessageRole.STUDENT
            )
            msg_content = match.group(3).strip()
            # Remove leading indentation from content lines
            msg_content = "\n".join(
                line[2:] if line.startswith("  ") else line
                for line in msg_content.split("\n")
            )

            conv["messages"].append(
                {
                    "timestamp": timestamp,
                    "role": role,
                    "content": msg_content,
                }
            )

        if conv.get("id"):
            conversations.append(conv)

    return assignment, conversations


def seed_db(transcript_path: str):
    with Session(engine) as session:
        existing = session.exec(select(Assignment)).first()
        if existing:
            print("Database already seeded.")
            return

        print("No existing data found. Parsing transcript and seeding database...")
        assignment_data, conversations_data = parse_transcript(transcript_path)

        # Create assignment
        assignment = Assignment(**assignment_data)
        session.add(assignment)

        # Create conversations and messages
        for conv_data in conversations_data:
            messages_data = conv_data.pop("messages")
            conv = Conversation(**conv_data, assignment_id=assignment.id)
            session.add(conv)

            for msg_data in messages_data:
                msg = Message(**msg_data, conversation_id=conv.id)
                session.add(msg)

        session.commit()
        print(f"Seeded {len(conversations_data)} conversations.")


def get_session():
    with Session(engine) as session:
        yield session
