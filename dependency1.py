from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

def get_settings():
    return {
        "app_name": "My API",
        "debug": True,
    }

@app.get("/info")
def get_info(settings: Annotated[dict, Depends(get_settings)]):
    return {
        "name": settings["app_name"],
        "debug": settings["debug"]
    }