#Что не так в этом коде?

# @app.get("/items")
# async def get_items():
#     response = requests.get("https://example.org/data")
#     return response.json()


"""Проблема в том, что внутри async endpoint используется блокирующий HTTP-клиент requests.
Это блокирует event loop и ухудшает производительность.

Правильно:"""

import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def get_items():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get("https://example.org/data")
        response.raise_for_status()
        return response.json()
    
    
"""
async полезен только при неблокирующем стеке;
таймауты обязательны;
стоит переиспользовать клиент, а не создавать его на каждый запрос, если архитектура это позволяет.
"""