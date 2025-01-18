import pygame


class Empty: # the base game object that is used as the parent to all game objects
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

        self.delete_me = False

    def update(self):
        pass

    def draw(self, window:pygame.Surface):
        pass

gameobjects_in_scene = []

def clear_all_gameobjects():
    global gameobjects_in_scene

    gameobjects_in_scene = []