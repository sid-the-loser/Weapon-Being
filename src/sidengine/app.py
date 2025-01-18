import pygame
from sidengine.gameobject import gameobjects_in_scene, Empty
import asyncio
import os

class App:
    def __init__(self, window_size=(600, 600), window_title="sidengine", window_flags=0, fps=60, vsync=True, display=0,
                 background=(0, 0, 0)):
        self.window_size = window_size
        self.window_title = window_title
        self.window_flags = window_flags
        self.fps = fps
        self.vsync = vsync
        self.display = display
        self.background = background

        self.running = True

        self.window = None
        self.clock = pygame.time.Clock()

        self.update_paused = False
        self.screen_drawover = True

    def exit(self):
        pass

    def init(self):
        pygame.init()
        if 'PYGAME_HIDE_SUPPORT_PROMPT' not in os.environ:
            print("Running SidEngine, a custom engine built on top of pygame :)")

        self.window = pygame.display.set_mode(size=self.window_size, flags=self.window_flags, display=self.display,
                                              vsync=self.vsync)
        pygame.display.set_caption(title=self.window_title)

    async def run(self):
        while self.running:
            self.clock.tick()

            self.early_extra_functions()

            if self.screen_drawover:
                self.window.fill(self.background)

            self.object_update_and_draw()
            pygame.display.flip()

            self.extra_functions()

            self.events()

            self.late_extra_functions()

            await asyncio.sleep(0)

        self.exit()

    def early_extra_functions(self):
        pass

    def extra_functions(self):
        pass

    def late_extra_functions(self):
        pass

    def object_update_and_draw(self):
        gameobject: Empty
        for gameobject in gameobjects_in_scene:
            if not self.update_paused:
                gameobject.update()

            gameobject.draw(self.window)

            if gameobject.delete_me:
                gameobjects_in_scene.remove(gameobject)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False