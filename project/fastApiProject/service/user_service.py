from project.fastApiProject.dtos import UserDTO
from project.fastApiProject.db import db
from project.fastApiProject.util.obj_mapper import to_entity
from project.fastApiProject.validation.signup_validation import validate

class UserService:

    def signup(user_dto: UserDTO):
        validate(user_dto)
        user_entity = to_entity(user_dto)
        db.session.add(user_entity)
        db.session.commit()