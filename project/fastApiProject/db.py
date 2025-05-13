from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeBase

db = create_engine('sqlite:///example.db', echo=True)

class BaseModel(DeclarativeBase):
    pass