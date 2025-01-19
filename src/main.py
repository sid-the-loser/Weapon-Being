import asyncio
from sidengine.app import App

myapp = App()

myapp.init()

async def main():
    await myapp.run()

asyncio.run(main())