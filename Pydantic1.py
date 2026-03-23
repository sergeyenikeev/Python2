from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator
from typing import Optional


class User(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=120)
    email: EmailStr
    is_active: bool = True
    city: Optional[str] = None

    # alias: можно передавать userName вместо name
    username: str = Field(alias="userName", min_length=3)

    @field_validator("name")
    @classmethod
    def name_must_be_title_case(cls, value: str) -> str:
        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")
        return value


# Корректные данные
data = {
    "id": "123",              # str -> будет преобразовано в int
    "name": "Sergey",
    "age": 30,
    "email": "sergey@example.com",
    "userName": "senikeev11"
}

user = User(**data)

print("Объект модели:")
print(user)

print("\nКак dict:")
print(user.model_dump())

print("\nКак JSON:")
print(user.model_dump_json(indent=2))


# Некорректные данные
bad_data = {
    "id": "abc",
    "name": "sergey",
    "age": 200,
    "email": "not-an-email",
    "userName": "ab"
}

try:
    bad_user = User(**bad_data)
except ValidationError as e:
    print("\nОшибки валидации:")
    print(e)