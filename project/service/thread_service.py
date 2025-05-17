from project.db import SessionLocal
from project.models import ThreadEntity


class ThreadService:
    def get_threads(page: int, size: int, offset: int):
        session = SessionLocal()
        query = session.query(ThreadEntity).order_by(ThreadEntity.date_created.desc())

        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)

        session.close()
        return query.all()
