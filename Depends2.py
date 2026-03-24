from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

class FakeDBSession:
    def __init__(self):
        self.connected = True

    def close(self):
        self.connected = False

    def get_users(self):
        return [{"id": 1, "name": "Alice"}]

def get_db():
    db = FakeDBSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Annotated[FakeDBSession, Depends(get_db)]):
    return db.get_users()