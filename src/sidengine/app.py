import pygame
import asyncio
from sidengine.colors import *

class App:
    def __init__(self):
        self.window = None

        self.window_size = (600, 600)
        self.window_title = "Untitled SidEngine Game"

        self.running = True

        self.scenes = []
        self.current_scene_index = 0

    def init(self):
        pygame.init()

        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

    async def run(self):
        while self.running:
            self.window.fill(BLACK)

            if len(self.scenes) > 0:
                self.scenes[0].events()
                self.scenes[0].update()
                self.scenes[0].draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            await asyncio.sleep(0)

class Scene:
    def __init__(self):
        pass

    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def events(self):
        pass