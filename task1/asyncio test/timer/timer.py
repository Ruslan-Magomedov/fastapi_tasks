"""
Декоратор для измерения времени работы асинхронной функции
"""

import time


def atimer(function):
    async def wrapper(*args, **kwargs):
        start = time.time()
        await function(*args, **kwargs)
        data = [*args]
        print(data[1], "запросов к REST API: ", data[0])
        print(f"Нагрузочное тестирование завершилось за {time.time() - start:.2f} секунд")
    return wrapper
