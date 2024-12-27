import asyncio

async def get_data():
    await asyncio.sleep(1)
    print("AAAAA1")
    return "Data"

async def process_data(data: str):
    await asyncio.sleep(2)
    print("AAAAA2")
    return data.upper()


async def main():
    data = await get_data()
    process_data(data)

asyncio.run(main())
