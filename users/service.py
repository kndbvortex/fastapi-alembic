from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models import User
from users.schemas import CreateUser
class UserService:
    def __init__(self, session:AsyncSession) -> None:
        self.session = session

    async def get_all_users(self):
        statement = select(User)
        result = await self.session.exec(statement)
        return result.all()

    async def create_user(self, user_data: CreateUser):
        new_user = User(**user_data.model_dump())
        self.session.add(new_user)
        await self.session.commit()
        return new_user