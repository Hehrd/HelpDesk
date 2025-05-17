from typing import Optional

from fastapi import APIRouter, Query
from starlette.responses import JSONResponse

from project.service.thread_service import ThreadService
from project.util.obj_mapper import to_thread_response_dto

thread_router = APIRouter()
thread_service = ThreadService()

@thread_router.get("/threads")
def get_threads(page: int = Query(0, ge=0, description="Page number"),
    size: int = Query(10, gt=0, le=100, description="Page size"),
    offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")):
    threads = thread_service.get_threads(page=page, size=size, offset=offset)
    return JSONResponse(content= {"threads": to_thread_response_dto(thread_entity) for thread_entity in threads},
                        status_code=200)

@thread_router.get("/threads/{id}")
def get_thread():
    return JSONResponse(status_code=200)

@thread_router.post("/threads")
def post_thread():
    return JSONResponse(status_code=201)

@thread_router.delete("/threads/{id}")
def delete_thread():
    return JSONResponse(status_code=204)