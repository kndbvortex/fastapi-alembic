from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from http import HTTPStatus
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from database import get_session
from users.service import UserService
from users.schemas import UserResponse, CreateUser, UpdateUser, BaseComputerSchema, UserWithComputerSchema
from models import User, Computer

user_router = APIRouter(prefix="/users")


@user_router.get("/", response_model=List[UserResponse])
async def read_users(session: AsyncSession = Depends(get_session), active: bool = True):
    return await UserService(session).get_all_users()


@user_router.post("/", status_code=HTTPStatus.CREATED)
async def create_user(user_data:CreateUser,session: AsyncSession = Depends(get_session)):
    print(user_data)
    return await UserService(session).create_user(user_data)


@user_router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@user_router.get("/{username}")
async def read_user(username: str, session: AsyncSession = Depends(get_session)):
    statement = select(User).where(User.username == username)
    return (await session.exec(statement)).one()


@user_router.put("/{username}")
async def update_user(username: str, user_info: UpdateUser, session: AsyncSession = Depends(get_session)):
    user = (await session.exec(select(User).where(User.username == username))).one()
    user_info = user_info.model_dump()
    for key in user_info:
        setattr(user, key, user_info[key])
    session.add(user)
    await session.commit()
    session.refresh(user)
    return user


@user_router.delete("/{username}", status_code=HTTPStatus.NO_CONTENT)
async def delete_user(username: str, session: AsyncSession = Depends(get_session)):
    user = (await session.exec(select(User).where(User.username == username))).one()
    session.delete(user)
    await session.commit()
    session.refresh(user)


@user_router.post("/{username}/create-computer", status_code=HTTPStatus.CREATED)
async def create_computer(username, computer_info: BaseComputerSchema, session: AsyncSession = Depends(get_session)):
    user = (await session.exec(select(User).where(User.username == username))).one()
    computer = Computer(user=user, **computer_info.model_dump())
    session.add(computer)
    await session.commit()
    return computer


@user_router.get("/{username}/user-with-computer", status_code=HTTPStatus.OK, response_model=UserWithComputerSchema)
async def read_user_computers(username: str, session: AsyncSession = Depends(get_session)):
    user = (await session.exec(select(User).where(User.username == username))).one()
    if user:
        computers = (await session.exec(select(Computer).where(Computer.user == user))).all()
        for computer in computers:
            print(computer.user, end=" !!!! \n\n\n")
        return UserWithComputerSchema(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            active=user.active,
            computers=[dict((col, getattr(row, col)) for col in row.__table__.columns.keys()) for row in computers]
        )
    return None

