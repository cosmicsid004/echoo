from pydantic import BaseModel
from typing import List
from datetime import datetime

# Schema for creating an eecho
class EechoCreate(BaseModel):
    body: str
    timeStamp: datetime

class ShowEecho(BaseModel):
    body: str
    class Config():
        orm_mode = True

# Schema for creating a new user
class UserCreate(BaseModel):
    username: str
    name: str 
    email: str
    password: str
    disabled: bool | None = None

class ShowUser(BaseModel):
    name: str
    username: str
    eechos: List[ShowEecho] = []
    class Config():
        orm_mode = True

class UserInDB(ShowUser):
    hash_password: str

class Login(BaseModel):
    username: str
    password: str

class ShowEechoWithCreator(BaseModel):
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None

class UserInDB(BaseModel):
    hashed_password: str

'''
| Class       | Purpose                             | Used for                             |
| ----------- | ----------------------------------- | ------------------------------------ |
| `Token`     | Structure of login response         | When returning the access token      |
| `TokenData` | Whats stored in the JWT            | When decoding and validating a token |
| `UserInDB`  | How a user's credentials are stored | Internally for password verification |
'''