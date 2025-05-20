from fastapi import APIRouter, Cookie
from starlette.responses import JSONResponse

from project.dtos import BugRequestDTO
from project.service.bugs_service import BugsService

bugs_router = APIRouter()
bugs_service = BugsService()

@bugs_router.get("/bugs/{thread_id}")
def get_bugs_by_thread_id(thread_id: int, jwt: str = Cookie(...)):
    bug_dtos = bugs_service.get_bugs_by_thread_id()
    return JSONResponse(content={"bugs": [bug_dto.as_dict() for bug_dto in bug_dtos]}, status_code=200)

@bugs_router.get("/bugs/{id}")
def get_bug_by_id(id: int, jwt: str = Cookie(...)):
    bug_dto = bugs_service.get_bug_by_id(bug_id=id, jwt=jwt)
    return JSONResponse(content=bug_dto.as_dict(), status_code=200)

@bugs_router.post("/bugs")
def post_bug(bug_dto: BugRequestDTO, jwt: str = Cookie(...)):
    bugs_service.create_bug(bug_dto=bug_dto, jwt=jwt)
    return JSONResponse(content=bug_dto.as_dict(), status_code=201)

@bugs_router.delete("/bugs/{id}")
def delete_bug():
    return JSONResponse(content=None, status_code=204)