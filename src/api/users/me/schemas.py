from pydantic import BaseModel


class UserJWTResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    access_token: str | None

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
