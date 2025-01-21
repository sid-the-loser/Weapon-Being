import pygame
import asyncio
from sidengine.color import *

class App:
    def __init__(self):
        self.window: pygame.Surface
        self.window = None

        self.window_size = (600, 600)
        self.window_title = "Untitled SidEngine Game"

        self.clock = pygame.time.Clock()
        self.dt = 1

        self.running = True

        self.scenes: tuple[Scene]
        self.scenes = []
        self.current_scene_index = 0

    def init(self):
        pygame.init()

        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

    def change_scene(self, scene_index):
        self.scenes[self.current_scene_index].init_ran = False
        self.current_scene_index = scene_index

    async def run(self):
        while self.running:
            self.window.fill(BLACK)
            self.dt = self.clock.tick() / 1000 # convertion to seconds from milliseconds

            if len(self.scenes) > 0:
                if not self.scenes[self.current_scene_index].init_ran:
                    self.scenes[self.current_scene_index].init()
                    self.scenes[self.current_scene_index].init_ran = True
                self.scenes[self.current_scene_index].update()
                self.scenes[self.current_scene_index].draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif len(self.scenes) > 0:
                    self.scenes[self.current_scene_index].events(event)

            pygame.display.flip()
            await asyncio.sleep(0)


class Scene:
    def __init__(self):
        self.init_ran = False

    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def events(self, event: pygame.event):
        pass