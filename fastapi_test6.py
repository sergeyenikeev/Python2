# Импорты необходимых библиотек
from fastapi import FastAPI  # FastAPI для создания веб-приложения
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  # Асинхронная работа с SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker  # ORM для работы с базой данных
from sqlalchemy import select  # Для выполнения SQL-запросов
from pydantic import BaseModel  # Для валидации данных
import httpx  # Для асинхронных HTTP-запросов

# Создание экземпляра FastAPI приложения
app = FastAPI()

# Настройка подключения к базе данных (SQLite для простоты)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True для логирования SQL-запросов
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # Фабрика сессий

# Базовый класс для моделей SQLAlchemy
class Base(DeclarativeBase):
    pass

# Модель пользователя для базы данных
class User(Base):
    __tablename__ = "users"  # Имя таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True)  # Первичный ключ
    name: Mapped[str]  # Поле имени пользователя

# Асинхронная функция для инициализации базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Создание всех таблиц

# Обработчик события запуска приложения
@app.on_event("startup")
async def on_startup():
    await init_db()  # Инициализация базы данных при старте

# Pydantic модели для валидации входных и выходных данных
class UserCreate(BaseModel):
    name: str  # Модель для создания пользователя (только имя)

class UserResponse(BaseModel):
    id: int  # Модель ответа с ID и именем
    name: str

# Эндпоинт для создания нового пользователя
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    async with async_session() as session:  # Создание асинхронной сессии
        db_user = User(name=user.name)  # Создание объекта пользователя
        session.add(db_user)  # Добавление в сессию
        await session.commit()  # Сохранение в базе данных
        await session.refresh(db_user)  # Обновление объекта с ID
        return db_user  # Возврат созданного пользователя

# Эндпоинт для получения списка всех пользователей
@app.get("/users/", response_model=list[UserResponse])
async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))  # Выполнение SELECT запроса
        users = result.scalars().all()  # Получение всех пользователей
        return users  # Возврат списка пользователей

# Эндпоинт для вызова внешнего REST API
@app.get("/external")
async def call_external():
    async with httpx.AsyncClient() as client:  # Создание асинхронного HTTP-клиента
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")  # GET-запрос к внешнему API
        return response.json()  # Возврат JSON-ответа

# Импорты для работы с потоками и задачами
import asyncio
import threading

# Функция для выполнения в отдельном потоке
def worker_function():
    print("Worker thread running")  # Вывод сообщения в консоль

# Асинхронная функция для выполнения задачи
async def task_function():
    await asyncio.sleep(1)  # Имитация асинхронной работы (ожидание 1 секунды)
    print("Async task completed")  # Вывод сообщения

# Эндпоинт для запуска worker-потока
@app.get("/run_worker")
async def run_worker():
    thread = threading.Thread(target=worker_function)  # Создание потока
    thread.start()  # Запуск потока
    return {"message": "Worker started"}  # Возврат сообщения

# Эндпоинт для запуска асинхронной задачи
@app.get("/run_task")
async def run_task():
    asyncio.create_task(task_function())  # Создание и запуск асинхронной задачи
    return {"message": "Task started"}  # Возврат сообщения

# Корневой эндпоинт
@app.get("/")
async def root():
    return {"message": "Hello World"}  # Возврат приветственного сообщения

# Эндпоинт для суммирования двух чисел
@app.get("/sum/")
async def calculate_sum(a: int, b: int):
    return {"result": a + b}  # Возврат результата сложения
