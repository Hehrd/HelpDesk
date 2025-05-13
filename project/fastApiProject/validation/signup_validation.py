import re

from project.fastApiProject.db import db
from project.fastApiProject.dtos import UserDTO
from project.fastApiProject.error.email_already_in_use_exception import EmailAlreadyInUseException
from project.fastApiProject.error.insufficient_data_exception import InsufficientDataException
from project.fastApiProject.error.missing_attributes_exception import MissingRequiredFieldsException
from project.fastApiProject.models import UserEntity


def validate(user_dto: UserDTO):
    validate_payload(user_dto)
    validate_email(user_dto.email)
    validate_first_name(user_dto.first_name)
    validate_last_name(user_dto.last_name)
    validate_password(user_dto.password)

def validate_payload(user_dto: UserDTO):
    if not user_dto.first_name or \
        not user_dto.last_name or \
        not user_dto.email or \
        not user_dto.password:
            raise MissingRequiredFieldsException("Missing required fields!")

def validate_email(email: str):
    if not email.endswith("@galactic_empire.org"):
        raise EmailAlreadyInUseException()
    if db.session.query(UserEntity).filter_by(email=email).first():
        raise EmailAlreadyInUseException(f"{email} is already in use!")

def validate_first_name(first_name: str):
    if len(first_name) < 2:
        InsufficientDataException("First name must be between least 2 and 50 letters long!")
    if not first_name.isalpha():
        raise InsufficientDataException("First name contains non-letter characters!")

def validate_last_name(last_name: str):
    if len(last_name) < 2:
        InsufficientDataException("Last name must be between least 2 and 50 letters long!")
    if not last_name.isalpha():
        raise InsufficientDataException("Last name must contain letter-only characters!")

def validate_password(password: str):
    if len(password) < 8 and len(password) > 50:
        raise InsufficientDataException("Password must be between 8 and 50 characters!")
    if not re.search(r'[a-zA-Z]', password):
        raise InsufficientDataException("Password must contain a letter!")
    if not re.search(r'\d', password):
        raise InsufficientDataException("Password must contain a digit!")
    if not re.search(r'[^\w]'):
        raise InsufficientDataException("Password must contain a symbol!")