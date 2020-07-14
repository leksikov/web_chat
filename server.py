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

"""

class RedisHandler():
    server_ = None
    def __init__(self, url_):
        self.server_ = await aioredis.create_redis(url_)
        return server_
    

    def close_connection(self):
        self.server_.close()
        self.server_.wait_close()

    def insert():


url = 'redis://localhost'
redis = RedisHandler(url)
"""     




async def hello(request):
    redis = await aioredis.create_redis('redis://localhost')
    await redis.set('main_param', 99)
    redis.close()
    await redis.wait_closed()
    return web.FileResponse("static/index.html")


async def login(request):
    param1 = request.rel_url.query['user_name']
    redis = await aioredis.create_redis('redis://localhost')
    await redis.hmset('user', 'name',  param1)
    await redis.hmset('user', 'ip_address',  request.remote)    
    await redis.sadd('visitors', param1)
    """
    await redis.set('user_name', param1)
    val = await redis.get('user_name')
    print(val)

    val2 = await redis.get('main_param')
    print(val2)
    """

    redis.close()
    await redis.wait_closed()
    
    #print("chatroom")
    return web.FileResponse("static/chatroom.html") #await chatroom(request)


async def chatroom(request):

    # display recent chat messages
    redis = await aioredis.create_redis('redis://localhost')
    current_user = await redis.hget('user', 'name')
    current_ip   = await redis.hget('user', 'ip_address')
    visitors = await redis.smembers('visitors')
    messages = await redis.smembers('messages')
    redis.close()
    await redis.wait_closed()

    print(type(messages))
    print(messages)
    return web.Response(text=str(current_user) + " " + str(visitors) + " " + str(messages))


async def current_user(request):
    redis = await aioredis.create_redis('redis://localhost')
    current_user = await redis.hget('user', 'name')
    #current_ip   = await redis.hget('user', 'ip_address')
    redis.close()
    await redis.wait_closed()    
    return web.Response(text=str(current_user))


async def users(request):
    redis = await aioredis.create_redis('redis://localhost')    
    visitors = await redis.smembers('visitors')
    redis.close()
    await redis.wait_closed()
    return web.Response(text=str(visitors))


async def send_message(request):
    param1 = request.rel_url.query['message']
    
    print("received message: ", param1)
    redis = await aioredis.create_redis('redis://localhost')
    current_user = await redis.hget('user', 'name')
    await redis.sadd('messages',   str(current_user) + ": " + param1)
    redis.close()
    await redis.wait_closed()
    return web.Response(text=f"message: {param1}")


async def get_messages(request):
    redis = await aioredis.create_redis('redis://localhost')
    messages = await redis.smembers('messages')
    redis.close()
    await redis.wait_closed()
    return web.Response(text=str(messages))


def main():

    app = web.Application()
    app.add_routes([web.get('/', hello),
                    web.get('/login', login),
                    web.get('/chatroom', chatroom),
                    web.get('/send_message', send_message),
                    web.get('/get_messages', get_messages),
                    web.get('/current_user', current_user),
                    web.get('/users', users)])
    web.run_app(app)

if __name__ == "__main__":
    main()
    