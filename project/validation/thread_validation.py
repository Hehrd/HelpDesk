from project.dtos import ThreadResponseDTO, ThreadRequestDTO
from project.error.null_body_exception import NullBodyException
from project.error.thread_not_found_exception import ThreadNotFoundException
from project.error.user_is_not_thread_creator_exception import UserIsNotThreadCreatorException
from project.models import ThreadEntity


def validate_thread(thread):
    if thread is None:
        raise ThreadNotFoundException("Thread not found!")

def validate_thread_request_dto(thread_request_dto: ThreadRequestDTO):
    if thread_request_dto is None:
        raise NullBodyException("Create thread request body is null!")

def validate_thread_creator(thread_creator_id: int, user_id: int):
    if not user_id == thread_creator_id:
        raise UserIsNotThreadCreatorException("You are not the creator of this thread!")

