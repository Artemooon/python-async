import asyncio
import aiohttp

async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def scrape_websites(urls: list[str]):
    tasks = [fetch_data(url) for url in urls]

    return await asyncio.gather(*tasks)

def main():
    websites = ["https://example.com/1",
                "https://example.com/2",
                "https://example.com/3"]

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(scrape_websites(websites))

    for res in results:
        print("result: {}".format(res))

main()