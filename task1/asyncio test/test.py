import aiohttp
import asyncio

from timer import timer


async def get_api_status(session, url):
    """ Выводим в консоль статус запроса """
    async with session.get(url) as response:
        print(f"Status: {response.status}")


@timer.atimer
async def main(url: str, n: int) -> None:
    """ Создаем сессию и отправляем n запросов в url """
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=500)) as session:
        tasks = [get_api_status(session, url) for _ in range(n)]
        await asyncio.gather(*tasks)

asyncio.run(main("http://localhost:8000/", 500))
