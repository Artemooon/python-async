
from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            print(f"Received text from client: {msg.data}")
            for ws_client in request.app["websockets"]:
                await ws_client.send_str(msg.data)
        elif msg.type == web.WSMsgType.ERROR:
            print(f"Websocket error: {ws.exception()}")

    return ws


app = web.Application()
app["websockets"] = []
app.router.add_get('/ws', websocket_handler)


if __name__ == '__main__':
    web.run_app(app)