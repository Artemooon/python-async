from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    for ws_client in request.app['websockets']:
        await ws_client.send_str("A new user has joined a chat")

    request.app['websockets'].append(ws)

    async for msg in ws:
        for ws_client in request.app['websockets']:
            await ws_client.send_str(msg.data)

    request.app['websockets'].remove(ws)
    return ws

app = web.Application()
app['websockets'] = []

app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    web.run_app(app)
