# This game is built using pygame and my engine!

from sidengine.app import App
import asyncio


# TODO: add a scene system that's inbuilt into the app

class MyApp(App):
    def __init__(self):
        super().__init__(window_title="Weapon Being")


game = MyApp()

game.init()

asyncio.run(game.run())