import json
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from project.models import LogLevels


class SignUpUserDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    def as_dict(self):
        return json.loads(self.json())

class LoginUserDTO(BaseModel):
    email: str
    password: str

    def as_dict(self):
        return json.loads(self.json())

class UserResponseDTO(BaseModel):
    first_name: str
    last_name: str
    email: str

    def as_dict(self):
        return json.loads(self.json())

class LogResponseDTO(BaseModel):
    id: int
    type:LogLevels
    file_name: str
    date_created: datetime
    bugs_ids: list[int]

    def as_dict(self):
        return json.loads(self.json())

class BugResponseDTO(BaseModel):
    id: int
    title: str
    log_ids: list[int]
    thread_id: int

    def as_dict(self):
        return json.loads(self.json())

class ThreadResponseDTO(BaseModel):
    id: int
    title: str
    description: str
    date_created: datetime
    bugs_ids: list[int]
    creator_id: int

    def as_dict(self):
        return json.loads(self.json())

class CommentResponseDTO(BaseModel):
    id: int
    text: str
    date_created: datetime
    is_edited: bool
    creator_id: int
    bug_id: int

    def as_dict(self):
        return json.loads(self.json())

class ThreadCreateRequestDTO(BaseModel):
    creator_id: Optional[int] = None
    title: str
    description: str
    date_created: Optional[datetime] = None

    def as_dict(self):
        return json.loads(self.json())

class BugCreateRequestDTO(BaseModel):
    creator_id: Optional[int] = None
    title: str
    thread_id: int

    def as_dict(self):
        return json.loads(self.json())

class LogAddToBugRequestDTO(BaseModel):
    id: int
    def as_dict(self):
        return json.loads(self.json())

class CommentCreateRequestDTO(BaseModel):
    creator_id: Optional[int] = None
    text: str
    date_created: Optional[datetime] = None
    bug_id: int

    def as_dict(self):
        return json.loads(self.json())

class CommentEditRequestDTO(BaseModel):
    text: str
    date_created: Optional[datetime] = None

    def as_dict(self):
        return json.loads(self.json())

class BugEditRequestDTO(BaseModel):
    title: str

    def as_dict(self):
        return json.loads(self.json())

class ThreadEditRequestDTO(BaseModel):
    title: str
    description: str

    def as_dict(self):
        return json.loads(self.json())
