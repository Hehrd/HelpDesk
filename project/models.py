from datetime import datetime
from enum import Enum

from sqlalchemy import Integer, String, DateTime, Table, Column, ForeignKey
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

bug_thread_association = Table(
    "bug_thread_association",
    BaseEntity.metadata,
    Column("bug_id", ForeignKey("bugs.id"), primary_key=True),
    Column("thread_id", ForeignKey("threads.id"), primary_key=True),
)

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
    thread: Mapped["ThreadEntity"] = relationship(back_populates="bugs")

class ThreadEntity(BaseEntity):
    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    bugs: Mapped[list["BugEntity"]] = relationship(back_populates="thread", cascade="all, delete-orphan")