from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Response, status, Query
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
    expires = datetime.now() + timedelta(hours=1)
    response = JSONResponse(user_dto.as_dict(), status_code=200)
    response.set_cookie(
        key="jwt",
        value=jwt,
        httponly=True,
        expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
        samesite="lax",
        secure=False,
    )
    return response

@user_router.get("/by-first-name/{first_name}")
def get_by_first_name(first_name: str, page: int = Query(0, ge=0, description="Page number"),
    size: int = Query(10, gt=0, le=100, description="Page size"),
    offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")):
    user_response_dtos = user_service.get_users_by_first_name(page=page,
                                                              size=size,
                                                              offset=offset,
                                                              first_name=first_name)
    return JSONResponse(content={"users": [user_response_dto.as_dict() for user_response_dto in user_response_dtos]}, status_code=200)

@user_router.get("/by-last-name/{last_name}")
def get_by_last_name(last_name: str, page: int = Query(0, ge=0, description="Page number"),
    size: int = Query(10, gt=0, le=100, description="Page size"),
    offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")):
    user_response_dtos = user_service.get_users_by_last_name(page=page,
                                                              size=size,
                                                              offset=offset,
                                                              last_name=last_name)
    return JSONResponse(content={"users": [user_response_dto.as_dict() for user_response_dto in user_response_dtos]}, status_code=200)


