import pygame as pg
import sys, copy, time

import helpers as h

pg.init()
clock = pg.time.Clock()
width, height = 800, 800

black = (0, 0, 0)
white = (255, 255, 255)
bg_gray = (250, 248, 239)


screen = pg.display.set_mode((width, height), pg.RESIZABLE)
pg.display.set_caption('Sudoku Solver')

moveFont = pg.font.Font("OpenSans-Regular.ttf", 40)
textFont = pg.font.Font("OpenSans-Regular.ttf", 40)
moveFont.bold = True

board = h.initial_state()
board_tiles = []


def draw_board():
    dim = width - 100

    board_back = pg.Rect(0, 0, dim, dim)
    board_back.center = (width // 2, height // 2)
    pg.draw.rect(screen, white, board_back, border_radius=5)

    for i in range(len(board)):
        tile_row = []
        for j in range(len(board)):
            tile_row.append(h.Tile())

        board_tiles.append(tile_row)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    draw_board()

    clock.tick(60)
    pg.display.flip()
