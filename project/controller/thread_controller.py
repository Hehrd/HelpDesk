from typing import Optional

from fastapi import APIRouter, Query, Cookie
from starlette.responses import JSONResponse

from project.dtos import ThreadRequestDTO
from project.service.thread_service import ThreadService
from project.util.obj_mapper import to_thread_response_dto

thread_router = APIRouter()
thread_service = ThreadService()

@thread_router.get("/threads")
def get_threads(page: int = Query(0, ge=0, description="Page number"),
    size: int = Query(10, gt=0, le=100, description="Page size"),
    offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")):
    thread_dtos = thread_service.get_threads(page=page, size=size, offset=offset)
    return JSONResponse(content= {"threads": thread_dto.as_dict() for thread_dto in thread_dtos},
                        status_code=200)

@thread_router.get("/threads/{id}")
def get_thread():
    thread_dto = thread_service.get_thread_by_id(thread_id=id)
    return JSONResponse(thread_dto.as_dict(), status_code=200)

@thread_router.post("/threads")
def post_thread(thread_dto: ThreadRequestDTO, jwt: str = Cookie(...)):
    thread_service.create_thread(thread_dto=thread_dto, jwt=jwt)
    return JSONResponse(thread_dto.as_dict(), status_code=201)

@thread_router.delete("/threads/{id}")
def delete_thread(id: int, jwt: str = Cookie(...)):
    thread_service.delete_thread_by_id(thread_id=id, jwt=jwt)
    return JSONResponse(status_code=204, content=None)
