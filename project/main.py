from fastapi import FastAPI

from project.controller.bugs_controller import bugs_router
from project.controller.comments_controller import comments_router
from project.controller.logs_controller import logs_router
from project.controller.thread_controller import thread_router
from project.controller.user_controller import user_router
from project.error import exception_handler
from project.error.exception_handler import register_error_handler

app = FastAPI()
app.include_router(router=user_router, prefix="/users", tags=["users"])
app.include_router(router=thread_router, prefix="/threads", tags=["threads"])
app.include_router(router=bugs_router, prefix="/bugs", tags=["bugs"])
app.include_router(router=logs_router, prefix="/logs", tags=["logs"])
app.include_router(router=comments_router, prefix="/comments", tags=["comments"])

register_error_handler(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
