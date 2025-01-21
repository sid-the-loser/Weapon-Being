import pygame
import asyncio
from sidengine.app import App, Scene
import file_locations as fl

myapp = App()

myapp.init()


class EngineSplashScreen(Scene):
    def __init__(self):
        self.count = None
        self.splash_time = None

        super().__init__()
        self.font = pygame.font.Font(fl.workbench_font, 42)
        self.text = self.font.render("Built with SidEngine", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(myapp.window_size[0] // 2, myapp.window_size[1] // 2))

        self.next_scene_index = 1

    def init(self):
        self.splash_time = 3
        self.count = 0

    def draw(self):
        myapp.window.blit(self.text, self.text_rect)

    def update(self):
        self.count += myapp.dt

        if self.count > self.splash_time:
            myapp.change_scene(self.next_scene_index)

    def events(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            myapp.change_scene(self.next_scene_index)


class DevSplashScreen(Scene):
    def __init__(self):
        super().__init__()
        self.count = None
        self.splash_time = None

        self.font = pygame.font.Font(fl.workbench_font, 42)
        self.text = self.font.render("A game by SidTheLoser", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(myapp.window_size[0] // 2, myapp.window_size[1] // 2))

        self.next_scene_index = 2

    def init(self):
        self.splash_time = 3
        self.count = 0

    def draw(self):
        myapp.window.blit(self.text, self.text_rect)

    def update(self):
        self.count += myapp.dt

        if self.count > self.splash_time:
            myapp.change_scene(self.next_scene_index)

    def events(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            myapp.change_scene(self.next_scene_index)


class TitleScreen(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(fl.spectral_sc, 42)
        self.text = self.font.render("Weapon beinG", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(myapp.window_size[0] // 2, myapp.window_size[1] // 2))

        self.font1 = pygame.font.SysFont("Times New Roman", 16)
        self.text1 = self.font1.render("Press any key to continue...", True, (255, 255, 255))
        self.text_rect1 = self.text1.get_rect(center=((myapp.window_size[0] // 2), (myapp.window_size[1] // 2)+(42+16)))

    def draw(self):
        myapp.window.blit(self.text, self.text_rect)
        myapp.window.blit(self.text1, self.text_rect1)

    def events(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            myapp.change_scene(0)


myapp.scenes = [EngineSplashScreen(), DevSplashScreen(), TitleScreen()]

async def main():
    await myapp.run()

asyncio.run(main())