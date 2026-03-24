from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int


user = User("Sergey", 35)

print(user)        # User(name='Sergey', age=35)
print(user.name)   # Sergey
print(user.age)    # 35