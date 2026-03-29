from typing import Annotated
from fastapi import FastAPI, Depends

api = FastAPI()

def get_data():
    return "hello world2"

@api.get("/")
async def root(message1: Annotated[str, Depends(get_data)]):
    return {"message": message1}
