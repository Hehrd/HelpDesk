from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from datetime import datetime, timedelta

from project.error.invalid_jwt_exception import InvalidJWTException

SECRET_KEY = "secret-dev-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt(subject: str) -> str:
    payload = {
        "sub": subject,
        "exp": ACCESS_TOKEN_EXPIRE_MINUTES
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        subject: str = payload.get("sub")
        return subject
    except JWTError:
        raise InvalidJWTException("Invalid token")
