from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import select
from pydantic import BaseModel
import httpx

app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()

class UserCreate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    async with async_session() as session:
        db_user = User(name=user.name)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

@app.get("/users/", response_model=list[UserResponse])
async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

@app.get("/external")
async def call_external():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()

import asyncio
import threading

def worker_function():
    print("Worker thread running")

async def task_function():
    await asyncio.sleep(1)
    print("Async task completed")

@app.get("/run_worker")
async def run_worker():
    thread = threading.Thread(target=worker_function)
    thread.start()
    return {"message": "Worker started"}

@app.get("/run_task")
async def run_task():
    asyncio.create_task(task_function())
    return {"message": "Task started"}

@app.get("/")
async def root():
    return {"message": "Hello World"}
# http://127.0.0.1:8001/docs#/
#  python -m uvicorn fastapi_test:app --reload --port 8001


@app.get("/sum/")
async def calculate_sum(a: int, b: int):
    return {"result": a + b}
