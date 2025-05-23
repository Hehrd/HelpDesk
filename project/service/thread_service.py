from datetime import datetime
from time import timezone

from project.db import SessionLocal
from project.dtos import ThreadRequestDTO
from project.error.user_is_not_thread_creator_exception import UserIsNotThreadCreatorException
from project.models import ThreadEntity
from project.util.jwt import verify_jwt
from project.util.obj_mapper import to_thread_response_dto, to_thread_entity


class ThreadService:
    def get_threads(self, page: int, size: int, offset: int):
        session = SessionLocal()
        query = session.query(ThreadEntity).order_by(ThreadEntity.date_created.desc())

        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)

        threads_entities = query.all()
        thread_response_dtos = [to_thread_response_dto(threads_entity) for threads_entity in threads_entities]
        session.close()
        return thread_response_dtos

    def get_thread_by_id(self, thread_id: int):
        print(f"thread_id: {thread_id}")
        session = SessionLocal()
        thread_entity = session.query(ThreadEntity).filter(ThreadEntity.id == thread_id).first()
        thread_response_dto = to_thread_response_dto(thread_entity)
        session.close()
        return thread_response_dto

    def create_thread(self, thread_dto: ThreadRequestDTO, jwt: str):
        creator_id = verify_jwt(jwt)
        print(creator_id)
        thread_dto.creator_id = creator_id
        thread_dto.date_created = datetime.utcnow()
        print(thread_dto.date_created)
        session = SessionLocal()
        thread_entity = to_thread_entity(thread_dto)
        session.add(thread_entity)
        session.commit()
        session.close()

    def delete_thread_by_id(self, thread_id: int, jwt: str):
        session = SessionLocal()
        thread = session.query(ThreadEntity).filter_by(id=thread_id).first()
        user_id = int(verify_jwt(jwt))
        if not user_id == thread.creator_id:
            raise UserIsNotThreadCreatorException("You are not the creator of this thread!")
        session.delete(thread)
        session.commit()
        session.close()
