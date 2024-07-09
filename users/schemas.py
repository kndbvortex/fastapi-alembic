from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from models import User

class UserResponse(BaseModel):
    id: Optional[int]
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    password: str
    active: Optional[bool]
    created_at: datetime
    last_login: Optional[datetime]


class CreateUser(BaseModel):
    username: str 
    first_name: Optional[str]
    last_name: Optional[str]
    password:str
    confirm_password:str
    active: Optional[bool]=True
    created_at: datetime = datetime.now()
    last_login: datetime = None


class UpdateUser(BaseModel):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)


class BaseComputerSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    brand: str
    model: str
    price: float = Field(gt=0)


class UserWithComputerSchema(BaseModel):
    id: Optional[int]
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    active: Optional[bool] = True
    computers: list[BaseComputerSchema]

    class Config:
        orm_mode = True
