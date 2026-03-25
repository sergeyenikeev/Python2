#Что не так в этом коде?

@app.get("/items")
async def get_items():
    response = requests.get("https://example.org/data")
    return response.json()


"""Проблема в том, что внутри async endpoint используется блокирующий HTTP-клиент requests.
Это блокирует event loop и ухудшает производительность."""