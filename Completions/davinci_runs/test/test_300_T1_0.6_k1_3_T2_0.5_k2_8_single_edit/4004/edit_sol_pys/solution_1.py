import asyncio
import logging
from typing import Dict

from aiohttp import web

logging.basicConfig(level=logging.INFO)


async def index(request: web.Request) -> web.Response:
    return web.Response(text="Hello world")


async def init(loop: asyncio.AbstractEventLoop) -> web.Application:
    app = web.Application(loop=loop)
    app.router.add_get('/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


if __name__ == '__main__':
    main()
