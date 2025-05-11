from fastapi import APIRouter
from starlette.responses import JSONResponse

thread_router = APIRouter()

@thread_router.get("/threads")
async def get_threads():
    return JSONResponse(status_code=200)

@thread_router.get("/threads/{id}")
async def get_thread():
    return JSONResponse(status_code=200)

@thread_router.post("/threads")
async def post_thread():
    return JSONResponse(status_code=201)

@thread_router.delete("/threads/{id}")
async def delete_thread():
    return JSONResponse(status_code=204)