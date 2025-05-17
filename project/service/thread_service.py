from project.db import SessionLocal
from project.models import ThreadEntity
from project.util.obj_mapper import to_thread_response_dto


class ThreadService:
    def get_threads(page: int, size: int, offset: int):
        session = SessionLocal()
        query = session.query(ThreadEntity).order_by(ThreadEntity.date_created.desc())

        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)

        session.close()
        threads_entities = query.all()
        return [to_thread_response_dto(threads_entity) for threads_entity in threads_entities]

    def get_thread_by_id(thread_id: int):
        session = SessionLocal()
        thread_entity = session.query(ThreadEntity).filter(ThreadEntity.id == thread_id).first()
        session.close()
        return to_thread_response_dto(thread_entity)

