from fastapi import APIRouter
from starlette.responses import JSONResponse

bugs_router = APIRouter()

@bugs_router.get("/bugs")
async def get_bugs():
    return JSONResponse(status_code=200)

@bugs_router.get("/bugs/{id}")
async def get_bug():
    return JSONResponse(status_code=200)

@bugs_router.post("/bugs")
async def post_bug():
    return JSONResponse(status_code=201)

@bugs_router.delete("/bugs/{id}")
async def delete_bug():
    return JSONResponse(status_code=204)