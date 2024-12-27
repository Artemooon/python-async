import asyncio
import aiohttp

async def fetch_data_from_url(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                print("Text type", type(await response.text()))
                print("Json type", type(await response.json()))
                print("Response status", response.status)
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            print("Client error", e)
        except aiohttp.HttpProcessingError as e:
            print("HttpProcessingError error", e)


async def download_file(url: str, destination: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(destination, "wb") as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print("File downloaded successfully")
            else:
                print("Error: ", response.status)

def process_chunk():
    pass

async def handle_response(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async for chunk in response.content.iter_chunked(1024):
                process_chunk(chunk)

async def main():
    url = "https://example.com/file.zip"
    destination = "file.zip"
    await download_file(url, destination)

asyncio.run(main())
