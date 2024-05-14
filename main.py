import pygame as pg
import sys, random

import helpers as h

pg.init()
clock = pg.time.Clock()
width, height = 800, 800

black = (0, 0, 0)
white = (255, 255, 255)
bg_gray = (51, 51, 51)
board_gray = (84, 84, 84)
tile_color = (227, 227, 227)
selected_color = (150, 187, 250)


screen = pg.display.set_mode((width, height), pg.RESIZABLE)
pg.display.set_caption('Sudoku Solver')

board = h.initial_state()
board_tiles = []
board_back = pg.Rect(0, 0, 0, 0)
selected = None


def draw_board():
    global board_tiles, board_back
    board_tiles = []
    dim = min(width, height) - 100
    tile_dim = dim//9
    line_width = 2
    dim = tile_dim*9+line_width*2

    board_back = pg.Rect(0, 0, dim, dim)
    board_back.center = (width // 2, height // 2)
    pg.draw.rect(screen, black, board_back)

    y_off = 0

    for i in range(len(board)):
        x_off = 0
        tile_row = []
        if i == 3 or i == 6:
            y_off += line_width

        for j in range(len(board)):
            if j == 3 or j == 6:
                x_off += line_width

            col = tile_color
            if selected == (i, j):
                col = selected_color

            tile = h.Tile(board_back.top+tile_dim*j+x_off, board_back.left+tile_dim*i+y_off, tile_dim, board[i][j], col)
            tile.draw(screen)
            tile_row.append(tile)

        board_tiles.append(tile_row)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if not board_back.collidepoint(event.pos):
                selected = None
            else:
                for i in range(len(board_tiles)):
                    for j in range(len(board_tiles)):
                        if board_tiles[i][j].rect.collidepoint(event.pos):
                            selected = (i, j)

        if selected and event.type == pg.KEYDOWN:
            num = int(event.key)-pg.K_0
            if 0 <= num < 10:
                board[selected[0]][selected[1]] = num

    width, height = screen.get_size()
    screen.fill(bg_gray)
    draw_board()

    clock.tick(60)
    pg.display.flip()
