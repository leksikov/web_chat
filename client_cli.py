import sys

import asyncio
import aiohttp
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
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def login(session, url):
    params = {'user_name': 'Sergey'}
    async with session.get(url, params=params) as response:
        return await response.text()

async def chatroom(session, url):
    params = {'user_name': 'Sergey'}
    async with session.get(url, params=params) as response:
        return await response.text()



async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://localhost:8080')
        print(html)
        

        html = await login(session, 'http://localhost:8080/login')
        print(html)

        html = await chatroom(session, 'http://localhost:8080/chatroom')
        print()
        print(html)
       
        

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
