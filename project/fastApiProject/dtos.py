from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class UserDTO:
    first_name: str
    last_name: str
    email: str
    password: str
    id: Optional[int] = None

    def as_dict(self):
        return asdict(self)
