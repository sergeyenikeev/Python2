# Пример FastAPI-приложения с асинхронной SQLite базой, внешним запросом и демонстрацией фоновой логики.
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import select
from pydantic import BaseModel
import httpx
import asyncio
import threading

app = FastAPI()

# Конфигурация асинхронного подключения к SQLite (файл test.db в корне проекта).
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True помогает увидеть SQL-запросы при отладке.
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """Базовый класс для ORM-моделей SQLAlchemy."""
    pass


class User(Base):
    """Простая модель пользователя с идентификатором и именем."""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


async def init_db():
    """Создает таблицы в базе данных при старте приложения."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    """Инициализирует базу данных при запуске FastAPI."""
    await init_db()


class UserCreate(BaseModel):
    """Схема для создания нового пользователя (только имя)."""
    name: str


class UserResponse(BaseModel):
    """Схема ответа с идентификатором и именем пользователя."""
    id: int
    name: str


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    """Сохраняет пользователя в БД и возвращает полученный record."""
    async with async_session() as session:
        db_user = User(name=user.name)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


@app.get("/users/", response_model=list[UserResponse])
async def get_users():
    """Возвращает всех пользователей из базы данных."""
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users


@app.get("/external")
async def call_external():
    """Пример вызова внешнего REST API с помощью httpx."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()


def worker_function():
    """Простая функция для демонстрации запуска отдельного потока."""
    print("Worker thread running")


async def task_function():
    """Асинхронная задача, имитирующая задержку и вывод в лог."""
    await asyncio.sleep(1)
    print("Async task completed")


@app.get("/run_worker")
async def run_worker():
    """Запускает worker-поток без ожидания завершения."""
    thread = threading.Thread(target=worker_function)
    thread.start()
    return {"message": "Worker started"}


@app.get("/run_task")
async def run_task():
    """Создает и запускает фоновую асинхронную задачу."""
    asyncio.create_task(task_function())
    return {"message": "Task started"}


@app.get("/")
async def root():
    """Базовый эндпоинт для проверки доступности сервиса."""
    return {"message": "Hello World"}


@app.get("/sum/")
async def calculate_sum(a: int, b: int):
    """Возвращает сумму двух целочисленных параметров."""
    return {"result": a + b}
