import asyncio

async def read_file():
    with open("data.txt") as file:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, file.read)
        print("Data: ", data)

asyncio.run(read_file())