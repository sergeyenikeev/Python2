from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

def get_message():
    return "hello"

@app.get("/")
def read_root(message: Annotated[str, Depends(get_message)]):
    return {"message": message}

