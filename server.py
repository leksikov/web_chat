import sys

import aioredis

from aiohttp import web
# tutorial for pyenv
# https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c
# https://dev.to/writingcode/the-python-virtual-environment-with-pyenv-pipenv-3mlo
"""
print("\n\n\n\n")
print(sys.executable)
print()
print(sys.version)
print(sys.path)
"""


async def hello(request):
    redis = await aioredis.create_redis('redis://localhost')
    await redis.set('main_param', 99)
    
    redis.close()
    await redis.wait_closed()
    return web.Response(text="Hello enter your user name:")


async def login(request):
    param1 = request.rel_url.query['user_name']
    
    redis = await aioredis.create_redis('redis://localhost')
    await redis.set('user_name', param1)
    val = await redis.get('user_name')
    print(val)

    val2 = await redis.get('main_param')
    print(val2)

    redis.close()
    await redis.wait_closed()

    return web.Response(text=f"Hello {param1}")


async def chatroom(request):

    # display recent chat messages
    return web.Response(text="All Chat room")

async def message(request):
    param1 = request.rel_url.query['message']
    # insert message to redis db
    return web.Response(text=f"message: {param1}")




app = web.Application()
app.add_routes([web.get('/', hello),
                web.get('/login', login),
                web.get('/chatroom', chatroom),
                web.get('/message', message)])

web.run_app(app)
