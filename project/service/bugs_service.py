from project.db import SessionLocal
from project.dtos import BugRequestDTO, LogResponseDTO, LogRequestDTO
from project.models import BugEntity, ThreadEntity, UserEntity, LogEntity
from project.util.jwt import verify_jwt
from project.util.obj_mapper import to_bug_response_dto, to_bug_entity, to_log_response_dto
from project.validation.bugs_validation import validate_bug
from project.validation.logs_validation import validate_log
from project.validation.thread_validation import validate_thread


class BugsService:
    def get_bugs_by_thread_id(self, thread_id: int, page: int, size: int, offset: int):
        session = SessionLocal()
        query = session.query(BugEntity).filter(BugEntity.thread_id == thread_id)
        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)
        bug_dtos = [to_bug_response_dto(bug_entity) for bug_entity in query.all()]
        session.close()
        return bug_dtos

    def get_bug_by_id(self, id: int, jwt: str):
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter(BugEntity.id == id).first()
        validate_bug(bug_entity)
        bug_dto = to_bug_response_dto(bug_entity)
        session.close()
        return bug_dto

    def create_bug(self, bug_request_dto: BugRequestDTO, jwt: str):
        session = SessionLocal()
        user_id = int(verify_jwt(jwt))
        bug_request_dto.creator_id = user_id
        thread = session.query(ThreadEntity).filter(ThreadEntity.id == bug_request_dto.thread_id).first()
        validate_thread(thread)
        bug_entity = to_bug_entity(bug_dto=bug_request_dto)
        session.add(bug_entity)
        session.commit()
        session.refresh(bug_entity)
        bug_respose_dto = to_bug_response_dto(bug_entity)
        session.close()
        return bug_respose_dto

    def delete_bug_by_id(self, id: int, jwt: str):
        user_id = verify_jwt(jwt)
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter(BugEntity.id == id, BugEntity.creator_id == user_id).first()
        validate_bug(bug_entity)
        session.delete(bug_entity)
        session.commit()

        session.close()

    def add_log(self, id: int, log_request_dto: LogRequestDTO, jwt: str):
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter(BugEntity.id == id).first()
        log_entity = session.query(LogEntity).filter(LogEntity.id == log_request_dto.id).first()
        validate_bug(bug_entity)
        validate_log(log_entity)
        bug_entity.logs.append(log_entity)
        session.commit()
        log_response_dto = to_log_response_dto(log_entity)
        session.close()
        return log_response_dto



