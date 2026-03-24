from typing import Annotated
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def get_token(x_token: str = Header(...)):
    return x_token

def get_current_user(token: Annotated[str, Depends(get_token)]):
    if token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "sergey"}

@app.get("/me")
def read_me(user: Annotated[dict, Depends(get_current_user)]):
    return user