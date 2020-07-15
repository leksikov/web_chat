
import aioredis

from aiohttp import web


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
    redis.close()
    await redis.wait_closed()
    return web.FileResponse("static/chatroom.html") #await chatroom(request)


async def current_user(request):
    redis = await aioredis.create_redis('redis://localhost')
    current_user = await redis.hget('user', 'name')
    current_user = current_user.decode("utf-8")

    redis.close()
    await redis.wait_closed()
    return web.Response(text=str(current_user))


async def users(request):
    redis = await aioredis.create_redis('redis://localhost')
    visitors = await redis.smembers('visitors')
    if len(visitors) > 0:
        visitors = [v.decode("utf-8") for v in visitors]
    redis.close()
    await redis.wait_closed()
    return web.Response(text=str(visitors))


async def send_message(request):
    param1 = request.rel_url.query['message']
    
    print("received message: ", param1)
    redis = await aioredis.create_redis('redis://localhost')
    current_user = await redis.hget('user', 'name')
    current_user = current_user.decode("utf-8")

    await redis.sadd('messages',   str(current_user) + ": " + param1)
    redis.close()
    await redis.wait_closed()
    return web.Response(text=f"message: {param1}")


async def get_messages(request):
    redis = await aioredis.create_redis('redis://localhost')
    messages = await redis.smembers('messages')
 
    if len(messages) > 0:
        messages = [str(x.decode("utf-8")) for x in messages]
    redis.close()
    await redis.wait_closed()
    return web.Response(text=str(messages))


def main():

    app = web.Application()
    app.add_routes([web.get('/', hello),
                    web.get('/login', login),
                    web.get('/send_message', send_message),
                    web.get('/get_messages', get_messages),
                    web.get('/current_user', current_user),
                    web.get('/users', users)])
    web.run_app(app)


if __name__ == "__main__":
    main()