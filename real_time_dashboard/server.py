import asyncio

from aiohttp import web

import random

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    while True:

        data = {"value": random.randint(0, 100)}
        await ws.send_json(data)
        await asyncio.sleep(5)


app = web.Application()

app.router.add_get('/ws', websocket_handler)


if __name__ == '__main__':
    web.run_app(app)
