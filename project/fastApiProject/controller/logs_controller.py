from fastapi import APIRouter
from starlette.responses import JSONResponse

logs_router = APIRouter()

@logs_router.get("/logs")
async def get_logs():
    return JSONResponse(status_code=200)

@logs_router.get("/logs/{id}")
async def get_log():
    return JSONResponse(status_code=200)

