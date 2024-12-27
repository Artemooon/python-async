import asyncio


async def tasks_cancellation():
    try:
        await asyncio.sleep(20)
    except asyncio.CancelledError:
        print("Cancelled")

async def main():
    task = asyncio.create_task(tasks_cancellation())
    await asyncio.sleep(2)
    task.cancel()

asyncio.run(main())
