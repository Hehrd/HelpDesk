from fastapi import APIRouter, Response, status
from starlette.responses import JSONResponse

from project.dtos import SignUpUserDTO, LoginUserDTO
from project.service.user_service import UserService

user_router = APIRouter()
user_service = UserService()
@user_router.post("/signup")
def signup(user_dto: SignUpUserDTO):
    user_service.signup(user_dto)
    return JSONResponse(user_dto.as_dict(), status_code=201)

@user_router.post("/login")
def login(user_dto: LoginUserDTO):
    jwt = user_service.login(user_dto)
    response = JSONResponse(user_dto.as_dict(), status_code=200)
    response.set_cookie(
        key="access_token",
        value=jwt,
        httponly=True,
        max_age=3600,
        samesite="lax",
        secure=False
    )
    return response

