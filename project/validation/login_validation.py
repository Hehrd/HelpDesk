from project.dtos import SignUpUserDTO, LoginUserDTO
from project.error.missing_required_fields_exception import MissingRequiredFieldsException


def validate_login(user_dto: LoginUserDTO):
    validate_payload(user_dto)

def validate_payload(user_dto: SignUpUserDTO):
    if not user_dto.email or not user_dto.password:
            raise MissingRequiredFieldsException("Missing required fields!")

