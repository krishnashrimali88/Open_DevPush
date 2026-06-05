import asyncio
import aiohttp
import os
from pathlib import Path

base = Path(os.path.dirname(__file__))

async def get():
    async with aiohttp.ClientSession() as session:

        async with session.get("http://127.0.0.1:8080/") as answer:
            tasks = await answer.json()

        for task in tasks:

            async with session.get(
                f"http://127.0.0.1:8080/files/{task}"
            ) as response:

                filepath = base /'to_do'/ task

                with open(filepath, "wb") as f:
                    async for chunk in response.content.iter_chunked(8192):
                        f.write(chunk)

                print(f"Downloaded: {task}")

asyncio.run(get())