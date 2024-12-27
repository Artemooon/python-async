import asyncio


class AsyncIter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count < self.iterable:
            await asyncio.sleep(1)
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration

async def main():
    async for item in AsyncIter(5):
        print("Number", item)

asyncio.run(main())
