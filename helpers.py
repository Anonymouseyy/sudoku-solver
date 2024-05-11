import pygame as pg


class Tile:
    def __init__(self, x=0, y=0, d=0, value=0, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.d = d
        self.value = value
        self.color = color
        self.rect = None

    def draw(self, surface, board_back):
        dim = board_back.width/9
        self.rect = pg.Rect(0, 0, dim, dim)
        self.rect.topleft = (self.x, self.y)

        pg.draw.rect(surface, self.color, self.rect, border_radius=2)


def initial_state():
    return [[0 for _ in range(9)] for _ in range(9)]
