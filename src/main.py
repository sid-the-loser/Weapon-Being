import pygame
import asyncio
from sidengine.app import App, Scene

myapp = App()

myapp.init()


class Testing(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('Arial', 40)
        self.text = self.font.render("Hello, World!", True, (255, 255, 255))

    def draw(self):
        text_rect = self.text.get_rect(center=(myapp.window_size[0] // 2, myapp.window_size[1] // 2))
        myapp.window.blit(self.text, text_rect)


myapp.scenes.append(Testing())

async def main():
    await myapp.run()

asyncio.run(main())