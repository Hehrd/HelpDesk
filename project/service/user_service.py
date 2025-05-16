from sqlalchemy.testing.pickleable import User

from project.dtos import SignUpUserDTO, LoginUserDTO
from project.db import db, SessionLocal
from project.models import UserEntity
from project.util.jwt import create_jwt
from project.util.obj_mapper import to_entity
from project.validation.login_validation import validate_login
from project.validation.signup_validation import validate_signup

class UserService:

    def signup(self, user_dto: SignUpUserDTO):
        validate_signup(user_dto)
        user_entity = to_entity(user_dto)
        session = SessionLocal()
        session.add(user_entity)
        session.commit()
        session.close()

    def login(self, user_dto: LoginUserDTO):
        validate_login(user_dto)
        # To be hashed
        password_hash = user_dto.password
        session = SessionLocal()
        user_entity = (session.query(UserEntity).filter(UserEntity.email == user_dto.email,
                                               UserEntity.password_hash == password_hash).first())
        session.close()
        print(user_entity)
        if user_entity:
           jwt = create_jwt(str(user_entity.id))
           return jwt