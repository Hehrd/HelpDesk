from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeBase, sessionmaker

db = create_engine('postgresql+psycopg://postgres:dev-pass@localhost:5432/db', echo=True)
SessionLocal = sessionmaker(bind=db, autoflush=False, autocommit=False)

class BaseEntity(DeclarativeBase):
    pass