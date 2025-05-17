from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from project.models import LogLevels


@dataclass
class SignUpUserDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    def as_dict(self):
        return asdict(self)

@dataclass
class LoginUserDTO:
    email: str
    password: str

    def as_dict(self):
        return asdict(self)

@dataclass
class LogResponseDTO:
    id: int
    type:LogLevels
    file_name: str
    date_created: datetime
    bugs_ids: list[int]

    def as_dict(self):
        return asdict(self)

@dataclass
class BugResponseDTO:
    id: int
    title: str
    log_ids: list[int]
    thread_id: int

    def as_dict(self):
        return asdict(self)

@dataclass
class ThreadResponseDTO:
    id: int
    title: str
    description: str
    date_created: datetime
    bugs_ids: list[int]
    creator_id: int

    def as_dict(self):
        return asdict(self)

@dataclass
class ThreadRequestDTO():
    creator_id: Optional[int]
    title: str
    description: str
    date_created: Optional[datetime]

    def as_dict(self):
        return asdict(self)
