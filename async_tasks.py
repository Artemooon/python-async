import asyncio

async def task1():
    try:
        print("Task 1 started")
        await asyncio.sleep(3)
        print("Task 1 completed")
        raise Exception("Something went wrong")
    except Exception as e:
        print(e)

async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 completed")
    return "task2 top"

async def main():
    # Create tasks from coroutines
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    done, pending = await asyncio.gather(t1, t2)

    for task in done:
        print("Task completed: ", task)
        print("Task completed: ", task.result())


asyncio.run(main())