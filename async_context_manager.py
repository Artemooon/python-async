import asyncio

class AsyncContextManager:

    async def __aenter__(self):
        print("Async context manager")
        await asyncio.sleep(1)
        print("Resource acquired")
        return "Context manager"

    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource")
        await asyncio.sleep(1)
        print("Resource released")


async def main():
    async with AsyncContextManager() as context:
        print("Using context manager", context)

asyncio.run(main())