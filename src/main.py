# This game is built using pygame and my engine!

from sidengine.app import App
import asyncio


class MyApp(App):
    def __init__(self):
        super().__init__(window_title="Weapon Being")


game = MyApp()

game.init()

asyncio.run(game.run())
