from typing import Annotated, Optional
from fastapi import FastAPI, Depends

app = FastAPI()

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, limit: int = 10):
        self.q = q
        self.limit = limit

@app.get("/items")
def read_items(params: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    return {
        "q": params.q,
        "limit": params.limit
    }