import pygame
import asyncio

from sidengine.app import App, Scene
from sidengine.color import *
from sidengine.gameobject import Empty, SimpleTextDisplay

import file_locations as fl

myapp = App()

myapp.window_title = "Weapon Being"

myapp.init()


class EngineSplashScreen(Scene):
    def __init__(self):
        self.count = None
        self.splash_time = None

        super().__init__()
        self.font = pygame.font.Font(fl.workbench_font, 42)
        self.text = self.font.render("Built with SidEngine", False, WHITE)
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
        self.text = self.font.render("A game by SidTheLoser", False, WHITE)
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
        self.text = self.font.render("Weapon beinG", False, WHITE)
        self.text_rect = self.text.get_rect(center=(myapp.window_size[0] // 2, myapp.window_size[1] // 2))

        self.font1 = pygame.font.SysFont("Times New Roman", 16)
        self.text1 = self.font1.render("Press any key to continue...", False, WHITE)
        self.text_rect1 = self.text1.get_rect(center=((myapp.window_size[0] // 2), (myapp.window_size[1] // 2)+(42+16)))

        self.next_scene_index = 3

    def draw(self):
        myapp.window.blit(self.text, self.text_rect)
        myapp.window.blit(self.text1, self.text_rect1)

    def events(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            myapp.change_scene(self.next_scene_index)


class LoreScene(Scene):
    def __init__(self):
        super().__init__()
        self.text_display_title = SimpleTextDisplay(
            text="Lore",
            font_location=fl.spectral_sc,
            is_sys_font=False,
            font_size=72,
            font_color=WHITE,
            x=myapp.window_size[0] // 2,
            y = 72 // 2,
            antialiasing=False
        )
        self.text_display = SimpleTextDisplay(
            text=open(fl.lore).read(),
            font_location="Times New Roman",
            is_sys_font = True,
            font_size=24,
            font_color=WHITE,
            x=myapp.window_size[0] // 2,
            y= (24 // 2) + 72 + 50,
            antialiasing=False
        )

        self.next_scene_index = 4

    def draw(self):
        self.text_display.draw(myapp.window)
        self.text_display_title.draw(myapp.window)

    def events(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            myapp.change_scene(self.next_scene_index)


class GameplayScene(Scene):
    def __init__(self):
        super().__init__()
        self.gameobject_list = []

    def update(self):
        gameobject: Empty
        for gameobject in self.gameobject_list:
            gameobject.update(myapp.dt)
            gameobject.draw(myapp.window)

    def draw(self):
        pass

    def events(self, event: pygame.event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                myapp.running = False

# All scenes that will be included in the build of the game
myapp.scenes = [EngineSplashScreen(), DevSplashScreen(), TitleScreen(), LoreScene(), GameplayScene()]

async def main():
    await myapp.run()

asyncio.run(main())