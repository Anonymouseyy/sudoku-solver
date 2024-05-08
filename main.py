import pygame as pg
import sys, copy, time

import helpers as h

pg.init()
clock = pg.time.Clock()
width, height = 600, 700

black = (0, 0, 0)
white = (255, 255, 255)
bg_gray = (250, 248, 239)


screen = pg.display.set_mode((width, height), pg.RESIZABLE)
pg.display.set_caption('Sudoku Solver')

moveFont = pg.font.Font("OpenSans-Regular.ttf", 40)
textFont = pg.font.Font("OpenSans-Regular.ttf", 40)
moveFont.bold = True

board = h.initial_state()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(60)
    pg.display.flip()
