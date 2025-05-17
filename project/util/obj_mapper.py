from xml.dom.minidom import Entity

from project.dtos import SignUpUserDTO, LogResponseDTO, ThreadResponseDTO, ThreadRequestDTO
from project.models import UserEntity, LogEntity, ThreadEntity


def to_user_entity(dto: SignUpUserDTO):
    user_entity = UserEntity()
    user_entity.first_name = dto.first_name
    user_entity.last_name = dto.last_name
    user_entity.email = dto.email
    user_entity.password_hash = dto.password
    return user_entity

def to_thread_entity(thread_dto: ThreadRequestDTO):
    thread_entity = ThreadEntity()
    thread_entity.creator_id = thread_dto.id
    thread_entity.title = thread_dto.title
    thread_entity.description = thread_dto.description
    return thread_entity


def to_log_response_dto(entity: LogEntity):
    log_response_dto = LogResponseDTO()
    log_response_dto.id = entity.id
    log_response_dto.type = entity.type
    log_response_dto.file_name = entity.file_name
    log_response_dto.date_created = entity.date_created
    log_response_dto.bugs_ids = [bug_entity.id for bug_entity in entity.bugs]
    return log_response_dto

def to_thread_response_dto(entity: ThreadEntity):
    thread_response_dto = ThreadResponseDTO()
    thread_response_dto.id = entity.id
    thread_response_dto.title = entity.title
    thread_response_dto.description = entity.description
    thread_response_dto.date_created = entity.date_created
    thread_response_dto.bugs_ids = [bug_entity.id for bug_entity in entity.bugs]
    return thread_response_dto
