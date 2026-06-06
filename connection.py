import aiohttp
import os
from pathlib import Path
from customtkinter import CTkCheckBox


base = Path(os.path.dirname(__file__))

async def down(addr):
    addr = Path(addr)
    async with aiohttp.ClientSession() as session:
    
        async with session.get("http://127.0.0.1:8080/") as answer:
            tasks = await answer.json()

        for task in tasks:

            async with session.get(
                f"http://127.0.0.1:8080/files/{task}"
            ) as response:

                
                new_path = addr / task


                with open(new_path, "wb") as f:
                    async for chunk in response.content.iter_chunked(8192):
                        f.write(chunk)

                print(f"Downloaded: {task}")

async def update(frame):
    for widget in frame.winfo_children():
        widget.destroy()


    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080/") as answer:
            tasks = await answer.json()
    
    for t in tasks:
        CTkCheckBox(frame,text=f'{t}').pack()






