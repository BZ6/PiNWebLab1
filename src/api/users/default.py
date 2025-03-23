from sqlmodel import SQLModel


# User table
class UserDefault(SQLModel):
    username: str
    email: str
