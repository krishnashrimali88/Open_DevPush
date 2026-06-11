import aiohttp
import os
from pathlib import Path
from customtkinter import CTkCheckBox

tasks = []
checkboxes = []



base = Path(os.path.dirname(__file__))

async def down(addr):
    selected_files = []
    global checkboxes

    for cb in checkboxes:
        if cb.get() == 1:
            selected_files.append(cb.cget('text'))

    addr = Path(addr)
 
    
    async with aiohttp.ClientSession() as session:
    
    
        for task in selected_files:
            async with session.get(f"http://127.0.0.1:8080/files/{task}") as response:
                new_path = addr / task

                with open(new_path, "wb") as f:
                    async for chunk in response.content.iter_chunked(8192):
                        f.write(chunk)

                print(f"Downloaded: {task}")




async def update(frame):
    global tasks
    global checkboxes
    checkboxes.clear()
    for widget in frame.winfo_children():
        widget.destroy()


    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080/") as answer:
            tasks = await answer.json()
    
    for t in tasks:
        temp = CTkCheckBox(frame,text=f'{t}')
        temp.pack()
        checkboxes.append(temp)






