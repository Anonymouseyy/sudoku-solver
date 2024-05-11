import pygame as pg

pg.init()
value_font = pg.font.Font("OpenSans-Regular.ttf", 30)


class Tile:
    def __init__(self, x=0, y=0, d=0, value=0, color=(227, 227, 227), text_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.d = d
        self.value = value
        self.color = color
        self.text_color = text_color
        self.rect = None

    def draw(self, surface):
        self.rect = pg.Rect(0, 0, self.d, self.d)
        self.rect.topleft = (self.x, self.y)

        pg.draw.rect(surface, self.color, self.rect)
        pg.draw.rect(surface, self.text_color, self.rect, width=1)

        if self.value:
            num = value_font.render(f'{self.value}', True, self.text_color)
            num_rect = num.get_rect()
            num_rect.center = self.rect.center
            surface.blit(num, num_rect)


def initial_state():
    return [[0 for _ in range(9)] for _ in range(9)]
