import sys


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
    
    return web.Response(text="Hello enter your user name:")


async def login(request):
    param1 = request.rel_url.query['user_name']

    # insert user name and session details into redis db

    return web.Response(text=f"Hello {param1}")


async def chatroom(request):

    # display recent chat messages
    return web.Response(text="Chat room")

async def message(request):

    # send message and insert to redis db
    return web.Response(text="Chat room")


app = web.Application()
app.add_routes([web.get('/', hello),
                web.get('/login', login),
                web.get('/chatroom', chatroom)])

web.run_app(app)
