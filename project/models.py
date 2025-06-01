from datetime import datetime
from enum import Enum

from sqlalchemy import Integer, String, DateTime, Table, Column, ForeignKey, Boolean
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from project.db import BaseEntity



class LogLevels(Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"

class UserEntity(BaseEntity):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[String] = mapped_column(String(50), nullable=False)
    last_name: Mapped[String] = mapped_column(String(50), nullable=False)
    email: Mapped[String] = mapped_column(String(50), nullable=False)
    password_hash: Mapped[String] = mapped_column(String(64), nullable=False)

log_bug_association = Table(
    "log_bug_association",
    BaseEntity.metadata,
    Column("log_id", ForeignKey("logs.id"), primary_key=True),
    Column("bug_id", ForeignKey("bugs.id"), primary_key=True),
)

comment_bug_association = Table(
    "comment_bug_association",
    BaseEntity.metadata,
    Column("comment_id", ForeignKey("comment.id"), primary_key=True),
    Column("bug_id", ForeignKey("bugs.id"), primary_key=True),
)

bug_thread_association = Table(
    "bug_thread_association",
    BaseEntity.metadata,
    Column("bug_id", ForeignKey("bugs.id"), primary_key=True),
    Column("thread_id", ForeignKey("threads.id"), primary_key=True),
)

class CommentEntity(BaseEntity):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[String] = mapped_column(String(200), nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_edited: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    creator: Mapped["UserEntity"] = relationship()
    bug_id: Mapped[int] = mapped_column(ForeignKey("bugs.id"), nullable=False)
    bug: Mapped["BugEntity"] = relationship(back_populates="comments")

class LogEntity(BaseEntity):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[LogLevels] = mapped_column(SQLEnum(LogLevels), name="level")
    file_name: Mapped[str] = mapped_column(String, nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    bugs: Mapped[list["BugEntity"]] = relationship(
        secondary=log_bug_association,
        back_populates="logs"
    )

class BugEntity(BaseEntity):
    __tablename__ = "bugs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)

    logs: Mapped[list["LogEntity"]] = relationship(
        secondary=log_bug_association,
        back_populates="bugs"
    )
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    creator: Mapped["UserEntity"] = relationship()

    thread_id: Mapped[int] = mapped_column(ForeignKey("threads.id"), nullable=False)
    thread: Mapped["ThreadEntity"] = relationship(back_populates="bugs")

    comments: Mapped[list["CommentEntity"]] = relationship(secondary=comment_bug_association, back_populates="bugs", cascade="all, delete-orphan")

class ThreadEntity(BaseEntity):
    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    creator: Mapped["UserEntity"] = relationship()
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    bugs: Mapped[list["BugEntity"]] = relationship(back_populates="thread", cascade="all, delete-orphan")