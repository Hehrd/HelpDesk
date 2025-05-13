from fastapi import APIRouter
from starlette.responses import JSONResponse

from project.fastApiProject.dtos import UserDTO
from project.fastApiProject.service.user_service import UserService

user_router = APIRouter()
user_service = UserService()
@user_router.post("/signup")
async def signup(user_dto: UserDTO):
    user_service.signup(user_dto)
    return JSONResponse(user_dto.as_dict(), status_code=201)
