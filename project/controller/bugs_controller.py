from typing import Optional

from fastapi import APIRouter, Cookie, Query
from starlette.responses import JSONResponse

from project.dtos import BugCreateRequestDTO, LogAddToBugRequestDTO, BugEditRequestDTO, LogRemoveFromBugRequestDTO
from project.service.bugs_service import BugsService

bugs_router = APIRouter()
bugs_service = BugsService()

# @bugs_router.get("/bugs/{thread_id}")
# def get_bugs_by_thread_id(thread_id: int,
#                           jwt: str = Cookie(...),
#                           page: int = Query(0, ge=0, description="Page number"),
#     size: int = Query(10, gt=0, le=100, description="Page size"),
#     offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")):
#         bug_dtos = bugs_service.get_bugs_by_thread_id(thread_id=thread_id,
#                                                       page=page,
#                                                       size=size,
#                                                       offset=offset)
#         return JSONResponse(content={"bugs": [bug_dto.as_dict() for bug_dto in bug_dtos]}, status_code=200)

@bugs_router.get("/{id}")
def get_bug_by_id(id: int, jwt: str = Cookie(...)):
    bug_dto = bugs_service.get_bug_by_id(id=id, jwt=jwt)
    return JSONResponse(content=bug_dto.as_dict(), status_code=200)

@bugs_router.post("")
def post_bug(bug_request_dto: BugCreateRequestDTO, jwt: str = Cookie(...)):
    bug_response_dto = bugs_service.create_bug(bug_request_dto=bug_request_dto, jwt=jwt)
    return JSONResponse(content=bug_response_dto.as_dict(), status_code=201)

@bugs_router.delete("/{id}")
def delete_bug(id: int, jwt: str = Cookie(...)):
    bugs_service.delete_bug_by_id(id=id, jwt=jwt)
    return JSONResponse(content=None, status_code=204)

@bugs_router.patch("/logs/{id}")
def add_log(id: int, log_request_dto: LogAddToBugRequestDTO, jwt: str = Cookie(...)):
    log_response_dto = bugs_service.add_log(id=id, log_request_dto=log_request_dto, jwt=jwt)
    return JSONResponse(content=log_response_dto.as_dict(), status_code=200)

@bugs_router.patch("/{id}")
def edit_bug(id: int, bug_edit_request_dto: BugEditRequestDTO, jwt: str = Cookie(...)):
    bug_response_dto = bugs_service.edit_bug_by_id(id=id, bug_edit_request_dto=bug_edit_request_dto, jwt=jwt)
    return JSONResponse(content=bug_response_dto.as_dict(), status_code=200)

@bugs_router.delete("/logs/{id}")
def remove_log(id: int, log_remove_request_dto: LogRemoveFromBugRequestDTO, jwt: str = Cookie(...)):
    log_response_dto = bugs_service.remove_log_from_bug(id=id, log_request_dto=log_remove_request_dto, jwt=jwt)
    return JSONResponse(content=None, status_code=204)