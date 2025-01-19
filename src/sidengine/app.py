import pygame
import asyncio

class App:
    def __init__(self):
        self.window = None
        self.window_size = (600, 600)
        self.window_title = "Untitled SidEngine Game"
        self.running = True

    def init(self):
        pygame.init()

        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

    async def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            await asyncio.sleep(0)
