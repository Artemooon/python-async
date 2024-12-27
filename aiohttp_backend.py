from aiohttp import web

async def process_data(data):
    return data["some"].upper()

async def handle_request(request):
    data = await request.json()
    processed_data = await process_data(data)
    return web.json_response(data=processed_data)

app = web.Application()
app.router.add_post("/process", handle_request)


if __name__ == '__main__':
    web.run_app(app)