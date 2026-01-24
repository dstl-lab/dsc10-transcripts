from datetime import datetime
from enum import Enum
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class MessageRole(str, Enum):
    STUDENT = "STUDENT"
    AI_TUTOR = "AI_TUTOR"


class Assignment(SQLModel, table=True):
    id: str = Field(primary_key=True)  # UUID from transcript
    course_id: str
    generated_at: Optional[datetime] = None
    total_interactions: Optional[int] = None
    total_conversations: Optional[int] = None

    conversations: List["Conversation"] = Relationship(back_populates="assignment")


class Conversation(SQLModel, table=True):
    id: str = Field(primary_key=True)  # UUID from transcript
    assignment_id: str = Field(foreign_key="assignment.id")
    question_id: str
    student_name: str
    student_email: str
    started_at: datetime
    message_count: Optional[int] = None

    assignment: Optional[Assignment] = Relationship(back_populates="conversations")
    messages: List["Message"] = Relationship(back_populates="conversation")


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: str = Field(foreign_key="conversation.id")
    role: MessageRole
    content: str
    timestamp: datetime

    conversation: Optional[Conversation] = Relationship(back_populates="messages")
