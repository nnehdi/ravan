from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class JournalSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    chat_id: Optional[int] = Field(default=None, foreign_key="chat.id")

    chat: Optional["Chat"] = Relationship(
        back_populates="session", sa_relationship_kwargs=dict(lazy="joined")
    )


class Chat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    session: Optional["JournalSession"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="chat"
    )
    messages: list["Message"] = Relationship(
        back_populates="chat", sa_relationship_kwargs=dict(lazy="joined")
    )


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    role: str = Field(nullable=False)
    content: str = Field(nullable=False)
    chat_id: Optional[int] = Field(default=None, foreign_key="chat.id")

    chat: Optional["Chat"] = Relationship(
        back_populates="messages",
    )
