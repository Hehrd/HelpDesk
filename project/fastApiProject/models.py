from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base

from project.fastApiProject.db import BaseModel


class UserEntity(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[String] = mapped_column(String(50), nullable=False)
    last_name: Mapped[String] = mapped_column(String(50), nullable=False)
    email: Mapped[String] = mapped_column(String(50), nullable=False)
    password_hash: Mapped[String] = mapped_column(String(64), nullable=False)