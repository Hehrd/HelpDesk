from project.db import SessionLocal
from project.dtos import BugRequestDTO
from project.models import BugEntity, ThreadEntity, UserEntity
from project.util.jwt import verify_jwt
from project.util.obj_mapper import to_bug_response_dto, to_bug_entity


class BugsService:
    def get_bugs_by_thread_id(thread_id: int, page: int, size: int, offset: int):
        session = SessionLocal()
        query = session.query(BugEntity).filter(BugEntity.thread_id == thread_id)
        if offset is not None:
            query = query.offset(offset).limit(size)
        else:
            query = query.offset(page * size).limit(size)
        bug_dtos = [to_bug_response_dto(bug_entity) for bug_entity in query.all()]
        session.close()
        return bug_dtos

    def get_bug_by_id(bug_id: int, jwt: str):
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter(BugEntity.id == id).first()
        session.close()
        return to_bug_response_dto(bug_entity)

    def create_bug(bug_dto: BugRequestDTO, jwt: str):
        session = SessionLocal()
        user_id = int(verify_jwt(jwt))
        bug_dto.creator_id = user_id
        # thread = session.query(ThreadEntity).filter_by(id=bug_dto.thread_id).first()
        # user = session.query(UserEntity).filter_by(id=user_id).first()
        bug_entity = to_bug_entity(bug_dto=bug_dto)
        session.add(bug_entity)
        session.commit()
        session.refresh(bug_entity)
        session.close()

    def delete_bug_by_id(bug_id: int):
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter_by(id=bug_id).first()
        session.delete(bug_entity)
        session.commit()
        session.close()
