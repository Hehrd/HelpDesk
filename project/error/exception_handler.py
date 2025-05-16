from starlette.responses import JSONResponse

from project.error.email_already_in_use_exception import EmailAlreadyInUseException
from project.error.email_not_in_organization_exception import EmailNotInOrganizationException
from project.error.insufficient_data_exception import InsufficientDataException
from project.error.invalid_jwt_exception import InvalidJWTException
from project.error.missing_required_fields_exception import MissingRequiredFieldsException
from project.error.null_body_exception import NullBodyException
from fastapi import Request, FastAPI


def register_error_handler(app: FastAPI):
    @app.exception_handler(EmailAlreadyInUseException)
    def email_already_in_use(request: Request, exc: EmailAlreadyInUseException):
        return JSONResponse(status_code=409, content={"message": exc.msg})

    @app.exception_handler(EmailNotInOrganizationException)
    def email_not_in_org(request: Request, exc: EmailNotInOrganizationException):
        return JSONResponse(status_code=403, content={"message": exc.msg})

    @app.exception_handler(InsufficientDataException)
    def insufficient_data(request: Request, exc: InsufficientDataException):
        return JSONResponse(status_code=422, content={"message": exc.msg})

    @app.exception_handler(InvalidJWTException)
    def invalid_jwt(request: Request, exc: InvalidJWTException):
        return JSONResponse(status_code=401, content={"message": exc.msg})

    @app.exception_handler(MissingRequiredFieldsException)
    def missing_required_fields(request: Request, exc: MissingRequiredFieldsException):
        return JSONResponse(status_code=422, content={"message": exc.msg})

    @app.exception_handler(NullBodyException)
    def null_body(request: Request, exc: NullBodyException):
        return JSONResponse(status_code=422, content={"message": exc.msg})
