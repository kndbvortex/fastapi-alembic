from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer

class User(SQLModel, table=True):
    id: Optional[int] = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    username: str = Field(unique=True)
    first_name: Optional[str]
    last_name: Optional[str]
    password: str
    active: Optional[bool] = Field(default=True)
    created_at: datetime = Field(default=datetime.now)
    last_login: Optional[datetime] = Field(default=None)
    computers: List["Computer"] = Relationship(back_populates='user')

    model_config = {
        "arbitrary_types_allowed": True
    }

    def __repr__(self) -> str:
        return f"{self.id}-{self.username}"

    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name.upper()}"


class Computer(SQLModel, table=True):
    id: Optional[int] = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    brand: str
    model: str
    price: float = Field(gt=0)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="computers")

    model_config = {
        "arbitrary_types_allowed": True
    }