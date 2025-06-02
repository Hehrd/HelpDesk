from datetime import datetime

from project.db import SessionLocal
from project.dtos import CommentCreateRequestDTO, CommentEditRequestDTO
from project.models import CommentEntity, BugEntity
from project.util.jwt import verify_jwt
from project.util.obj_mapper import to_comment_response_dto, to_comment_entity
from project.validation.bugs_validation import validate_bug
from project.validation.comments_validation import validate_comment


class CommentsService:
    def get_comment_by_id(self, id: int):
        session = SessionLocal()
        comment_entity = session.query(CommentEntity).filter(CommentEntity.id == id).first()
        validate_comment(comment_entity)
        comment_response_dto = to_comment_response_dto(comment_entity)
        session.close()
        return comment_response_dto

    def create_comment(self, comment_create_request_dto: CommentCreateRequestDTO, jwt: str):
        user_id = verify_jwt(jwt)
        session = SessionLocal()
        bug_entity = session.query(BugEntity).filter(BugEntity.id == comment_create_request_dto.bug_id).first()
        validate_bug(bug_entity)
        comment_create_request_dto.creator_id = user_id
        comment_create_request_dto.date_created = datetime.utcnow()
        comment_entity = to_comment_entity(comment_create_request_dto)
        session.add(comment_entity)
        session.commit()
        session.refresh(comment_entity)
        comment_response_dto = to_comment_response_dto(comment_entity)
        session.close()
        return comment_response_dto

    def delete_comment(self, id: int, jwt: str):
        user_id = verify_jwt(jwt)
        session = SessionLocal()
        comment_entity = session.query(CommentEntity).filter(CommentEntity.id == id, CommentEntity.creator_id == user_id).first()
        validate_comment(comment_entity)
        session.delete(comment_entity)
        session.commit()

    def edit_comment(self, id: int, comment_edit_request_dto: CommentEditRequestDTO, jwt: str):
        user_id = verify_jwt(jwt)
        session = SessionLocal()
        comment_entity = session.query(CommentEntity).filter(CommentEntity.id == id, CommentEntity.creator_id == user_id).first()
        validate_comment(comment_entity)
        comment_entity.text = comment_edit_request_dto.text
        comment_entity.date_created = datetime.utcnow()
        comment_entity.is_edited = True
        session.commit()
        session.refresh(comment_entity)
        comment_response_dto = to_comment_response_dto(comment_entity)
        session.close()
        return comment_response_dto