from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
# http://127.0.0.1:8001/docs#/
#  python -m uvicorn fastapi_test:app --reload --port 8001


@app.get("/sum/")
async def calculate_sum(a: int, b: int):
    return {"result": a + b}
