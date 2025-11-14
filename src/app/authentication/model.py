from pydantic import BaseModel


class User(BaseModel):
    username:str
    password:str


class UserDb(User):
    hashed_password:str