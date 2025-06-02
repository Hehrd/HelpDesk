from fastapi import APIRouter, Cookie
from starlette.responses import JSONResponse

from project.dtos import CommentCreateRequestDTO, CommentEditRequestDTO
from project.service.comments_service import CommentsService

comments_router = APIRouter()
comments_service = CommentsService()

@comments_router.get("/{id}")
def get_comment(id: int):
    comment_response_dto = comments_service.get_comment_by_id(id=id)
    return JSONResponse(content=comment_response_dto.as_dict(), status_code=200)

@comments_router.post("")
def create_comment(comment_request_dto: CommentCreateRequestDTO, jwt: str = Cookie(...)):
    comment_response_dto = comments_service.create_comment(comment_request_dto, jwt)
    return JSONResponse(content=comment_response_dto.as_dict(), status_code=201)

@comments_router.delete("/{id}")
def delete_comment(id: int, jwt: str = Cookie(...)):
    comments_service.delete_comment(id=id, jwt=jwt)
    return JSONResponse(content=None, status_code=204)

@comments_router.patch("/{id}")
def edit_comment(id: int, comment_edit_request_dto: CommentEditRequestDTO, jwt: str = Cookie(...)):
    comment_response_dto = comments_service.edit_comment(comment_edit_request_dto=comment_edit_request_dto,
                                                         id=id,
                                                         jwt=jwt)
    return JSONResponse(content=comment_response_dto.as_dict(), status_code=200)
