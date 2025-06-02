from xml.dom.minidom import Entity

from project.dtos import SignUpUserDTO, LogResponseDTO, ThreadResponseDTO, ThreadCreateRequestDTO, BugResponseDTO, \
    BugCreateRequestDTO, CommentResponseDTO, CommentCreateRequestDTO, UserResponseDTO
from project.models import UserEntity, LogEntity, ThreadEntity, BugEntity, CommentEntity


def to_user_entity(dto: SignUpUserDTO):
    user_entity = UserEntity()
    user_entity.first_name = dto.first_name
    user_entity.last_name = dto.last_name
    user_entity.email = dto.email
    user_entity.password_hash = dto.password
    return user_entity

def to_thread_entity(thread_dto: ThreadCreateRequestDTO):
    thread_entity = ThreadEntity()
    thread_entity.creator_id = thread_dto.creator_id
    thread_entity.title = thread_dto.title
    thread_entity.description = thread_dto.description
    thread_entity.date_created = thread_dto.date_created
    return thread_entity

def to_bug_entity(bug_dto: BugCreateRequestDTO):
    bug_entity = BugEntity()
    bug_entity.creator_id = bug_dto.creator_id
    bug_entity.title = bug_dto.title
    bug_entity.thread_id = bug_dto.thread_id
    return bug_entity

def to_comment_entity(comment_dto: CommentCreateRequestDTO):
    comment_entity = CommentEntity()
    comment_entity.creator_id = comment_dto.creator_id
    comment_entity.text = comment_dto.text
    comment_entity.date_created = comment_dto.date_created
    comment_entity.bug_id = comment_dto.bug_id
    return comment_entity

def to_log_response_dto(entity: LogEntity):
    log_response_dto = LogResponseDTO(id=entity.id,
                                      type=entity.type,
                                      file_name=entity.file_name,
                                      date_created=entity.date_created,
                                      bugs_ids= [bug_entity.id for bug_entity in entity.bugs])
    return log_response_dto

def to_thread_response_dto(entity: ThreadEntity):
    thread_response_dto = ThreadResponseDTO(id=entity.id,
                                        creator_id=entity.creator_id,
                                        title=entity.title,
                                        date_created=entity.date_created,
                                        description=entity.description,
                                        bugs_ids=[bug_entity.id for bug_entity in entity.bugs])
    return thread_response_dto

def to_bug_response_dto(entity: BugEntity):
    bug_response_dto = BugResponseDTO(id=entity.id,
                                      creator_id=entity.creator_id,
                                      title=entity.title,
                                      thread_id=entity.thread_id,
                                      log_ids=[log_entity.id for log_entity in entity.logs])
    return bug_response_dto

def to_comment_response_dto(entity: CommentEntity):
    comment_response_dto = CommentResponseDTO(id=entity.id,
                                              creator_id=entity.creator_id,
                                              text=entity.text,
                                              date_created=entity.date_created,
                                              bug_id=entity.bug_id,
                                              is_edited=entity.is_edited)
    return comment_response_dto

def to_user_response_dto(entity: UserEntity):
    user_response_dto = UserResponseDTO(first_name=entity.first_name,
                                        last_name=entity.last_name,
                                        email=entity.email)
    return user_response_dto
