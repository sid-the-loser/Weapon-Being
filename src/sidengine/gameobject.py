import pygame

class Empty:
    def __init__(self, x:float=0, y:float=0) -> None:
        self.x = x
        self.y = y

    def update(self, dt: float) -> None:
        pass

    def draw(self, window: pygame.Surface) -> None:
        pass


class Sprite(Empty):
    def __init__(self, image_file_location:str, x:float=0, y:float=0) -> None:
        super().__init__(x=x, y=y)
        self.imported_image = pygame.image.load(image_file_location).convert()

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.imported_image, (self.x, self.y))


class SimpleAnimatedSprite(Empty):
    def __init__(self, image_file_location_array:list[str], x:float=0, y:float=0) -> None:
        super().__init__(x=x, y=y)
        self.imported_image_array = [pygame.image.load(filename).convert() for filename in image_file_location_array]
        self.current_index = 0
        self.accumulated_count = 0

    def update(self, dt: float) -> None:
        array_len = len(self.imported_image_array)
        if array_len > 0:
            self.accumulated_count += dt

            if round(self.accumulated_count) == 1:
                self.current_index += 1

                if self.current_index > array_len-1:
                    self.current_index = 0

                self.accumulated_count = 0

    def draw(self, window: pygame.Surface) -> None:
        if len(self.imported_image_array) > 0:
            window.blit(self.imported_image_array[self.current_index], (self.x, self.y))

class SimpleTextDisplay(Empty):
    def __init__(self, text:str, font_location:str, font_size:int, font_color:tuple[int], antialiasing=True, bold=False,
                 italic=False, constructor=None, is_sys_font=False, x:float=0, y:float=0) -> None:
        super().__init__(x=x, y=y)

        if is_sys_font:
            self.font = pygame.font.SysFont(font_location, font_size, bold, italic, constructor)
        else:
            self.font = pygame.font.Font(font_location, font_size)

        self.rendered_texts = []

        current_text_y = self.y

        for line in text.split("\n"):
            temp = []

            temp.append(self.font.render(line, antialiasing, font_color))
            temp.append(temp[0].get_rect(center=(self.x, current_text_y)))

            self.rendered_texts.append(temp)

            current_text_y += font_size

    def draw(self, window: pygame.Surface):
        for text in self.rendered_texts:
            window.blit(text[0], text[1])