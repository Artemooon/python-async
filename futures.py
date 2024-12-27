
import asyncio

async def task1():
    print("Starting task1")
    await asyncio.sleep(1)
    print("Task1 done")
    return "Task1 result"

async def main():
    future = asyncio.Future()

    asyncio.create_task(task1()).add_done_callback(lambda x: future.set_result("Task1 result"))
    await future

    print("Future result", future.result())

asyncio.run(main())