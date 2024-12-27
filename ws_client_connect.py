import aiohttp
import asyncio

async def connect_to_ws():

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            await ws.send_str("Hello World")
            async for msg in ws:
                print(f"Received message: {msg.data}")

asyncio.run(connect_to_ws())
