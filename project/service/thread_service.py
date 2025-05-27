from datetime import datetime
from time import timezone

from project.db import SessionLocal
from project.dtos import ThreadRequestDTO, BugRequestDTO
from project.error.user_is_not_thread_creator_exception import UserIsNotThreadCreatorException
from project.models import ThreadEntity
from project.util.jwt import verify_jwt
from project.util.obj_mapper import to_thread_response_dto, to_thread_entity
from project.validation.thread_validation import validate_thread, \
    validate_thread_request_dto, validate_thread_creator


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
        session = SessionLocal()
        thread_entity = session.query(ThreadEntity).filter(ThreadEntity.id == thread_id).first()
        thread_response_dto = to_thread_response_dto(thread_entity)
        session.close()
        validate_thread(thread_response_dto)
        return thread_response_dto

    def create_thread(self, thread_request_dto: ThreadRequestDTO, jwt: str):
        creator_id = verify_jwt(jwt)
        validate_thread_request_dto(thread_request_dto=thread_request_dto)
        thread_request_dto.creator_id = creator_id
        thread_request_dto.date_created = datetime.utcnow()

        session = SessionLocal()
        thread_entity = to_thread_entity(thread_request_dto)
        session.add(thread_entity)
        session.commit()
        thread_response_dto = to_thread_response_dto(thread_entity)
        session.close()
        return thread_response_dto

    def delete_thread_by_id(self, thread_id: int, jwt: str):
        session = SessionLocal()
        thread = session.query(ThreadEntity).filter_by(id=thread_id).first()
        user_id = int(verify_jwt(jwt))
        validate_thread_request_dto(thread)
        validate_thread_creator(thread_creator_id=thread.creator_id, user_id=user_id)
        session.delete(thread)
        session.commit()
        session.close()

