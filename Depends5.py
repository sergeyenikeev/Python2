from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

class UserRepository:
    def get_all(self):
        return [{"id": 1, "name": "Alice"}]

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def list_users(self):
        return self.repo.get_all()

def get_user_repository():
    return UserRepository()

def get_user_service(
    repo: Annotated[UserRepository, Depends(get_user_repository)]
):
    return UserService(repo)

@app.get("/users")
def list_users(service: Annotated[UserService, Depends(get_user_service)]):
    return service.list_users()