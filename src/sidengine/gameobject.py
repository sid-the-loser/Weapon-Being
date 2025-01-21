import pygame

class Empty:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, dt: float):
        pass

    def draw(self, window: pygame.Surface):
        pass


class Sprite(Empty):
    def __init__(self, image_file_location:str, x=0, y=0):
        super().__init__(x, y)
        self.imported_image = pygame.image.load(image_file_location).convert()

    def draw(self, window: pygame.Surface):
        window.blit(self.imported_image, (self.x, self.y))


class SimpleAnimatedSprite(Empty):
    def __init__(self, image_file_location_array:list[str], x=0, y=0):
        super().__init__(x, y)
        self.imported_image_array = [pygame.image.load(filename).convert() for filename in image_file_location_array]
        self.current_index = 0
        self.accumulated_count = 0

    def update(self, dt: float):
        array_len = len(self.imported_image_array)
        if array_len > 0:
            self.accumulated_count += dt

            if round(self.accumulated_count) == 1:
                self.current_index += 1

                if self.current_index > array_len-1:
                    self.current_index = 0

                self.accumulated_count = 0

    def draw(self, window: pygame.Surface):
        if len(self.imported_image_array) > 0:
            window.blit(self.imported_image_array[self.current_index], (self.x, self.y))