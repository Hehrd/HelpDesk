from xml.dom.minidom import Entity

from project.fastApiProject.dtos import UserDTO
from project.fastApiProject.models import UserEntity


def to_entity(dto: UserDTO):
    user_entity = UserEntity()
    user_entity.id = dto.id
    user_entity.first_name = dto.first_name
    user_entity.last_name = dto.last_name
    user_entity.email = dto.email
    user_entity.password_hash = dto.password_hash