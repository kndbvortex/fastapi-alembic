from fastapi import FastAPI
from users.router import user_router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    from database import init_db
    print("Server starting")
    await init_db()
    yield
    print("Shutting down")


app = FastAPI(
    title="FastApi with Postgres",
    description="Use FastApi with postgres",
    lifespan=lifespan
)


app.include_router(user_router, tags=["users"])


@app.get("")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello")
async def gretting():
    return {"message": "Hello, FastAPI!"}
