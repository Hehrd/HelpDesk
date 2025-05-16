from fastapi import FastAPI

from project.controller.user_controller import user_router
from project.error import exception_handler
from project.error.exception_handler import register_error_handler

app = FastAPI()
app.include_router(router=user_router, prefix="/users", tags=["users"])

register_error_handler(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
