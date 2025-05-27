from typing import Optional

from fastapi import APIRouter, Query
from starlette.responses import JSONResponse

from project.dtos import LogResponseDTO
from project.service.logs_service import LogsService

logs_router = APIRouter()
logs_service = LogsService()

# @logs_router.get("/logs/by-bug/{bug_id}")
# def get_logs_by_bug_id(
#     bug_id: int,
#     page: int = Query(0, ge=0, description="Page number"),
#     size: int = Query(10, gt=0, le=100, description="Page size"),
#     offset: Optional[int] = Query(None, ge=0, description="Override offset (optional)")
# ):
#     logs = logs_service.get_logs_by_bug_id(bug_id=bug_id, page=page, size=size, offset=offset)
#     return JSONResponse(content={"logs": [log_dto.as_dict() for log_dto in logs]}, status_code=200)

@logs_router.get("/logs/{id}")
def get_log(id: int):
    log_response_dto: LogResponseDTO = logs_service.get_log_by_id(id=id)
    return JSONResponse(content=log_response_dto.as_dict(), status_code=200)

