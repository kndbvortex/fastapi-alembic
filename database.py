import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession 
from sqlmodel import text
from sqlmodel import SQLModel
from sqlalchemy.orm.session import sessionmaker



load_dotenv()

async_engine = create_async_engine(
    os.getenv("DATABASE_URL"),
    echo=True
)

async def init_db():
    # async with AsyncSession(async_engine) as session:
    #     statement = text("SELECT 'hello Durande';")
    #     print(await session.exec(statement))
    async with async_engine.begin() as connexion:
        from models import User
        await connexion.run_sync(SQLModel.metadata.create_all)
        
        

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session