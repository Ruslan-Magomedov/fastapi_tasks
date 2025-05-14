from fastapi import FastAPI
import asyncio
import uvicorn

import random


app = FastAPI()


@app.get("/", summary="home page")
async def home() -> dict:
    """
    Асинхронная функция генерирует случайное число от 1 до 5
    затем засыпает n секунд и возвращает словарь
    """
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
