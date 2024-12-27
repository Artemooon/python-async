import asyncio

async def async_generator(limit: int):
    count = 0
    while count < limit:
        await asyncio.sleep(1)
        yield count
        count += 1

async def main():
    async for x in async_generator(10):
        print("Number", x)

asyncio.run(main())