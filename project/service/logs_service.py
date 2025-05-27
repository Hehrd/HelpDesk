
from project.db import SessionLocal
from project.models import LogEntity, BugEntity
from project.util.obj_mapper import to_log_response_dto
from project.validation.logs_validation import validate_log


class LogsService:

    def get_logs_by_bug_id(self, bug_id: int, page: int, size: int, offset: int):
        session = SessionLocal()
        query = (
            session.query(LogEntity)
            .join(BugEntity.logs)
            .filter(BugEntity.id == bug_id))

        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)

        log_entities = query.all()
        log_response_dtos = [to_log_response_dto(log_entity) for log_entity in log_entities]
        session.close()
        return log_response_dtos

    def get_log_by_id(self, id: int):
        session = SessionLocal()
        log_entity = session.query(LogEntity).filter(LogEntity.id == id).first()
        validate_log(log_entity)
        log_response_dto = to_log_response_dto(log_entity)
        session.close()
        return log_response_dto
