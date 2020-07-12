import sys


from aiohttp import web
# tutorial for pyenv
# https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c
# https://dev.to/writingcode/the-python-virtual-environment-with-pyenv-pipenv-3mlo

print("\n\n\n\n")
print(sys.executable)
print()
print(sys.version)
print(sys.path)




async def hello(request):
    return web.Response(text="hello world Seryoga")


def init_func(argv):
    app = web.Application()
    app.router.add_get("/", index_handler)
    return app
    
app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app)
