import pygame as pg
import sys, threading, random

import helpers as h
from sudoku import SudokuGame

pg.init()
clock = pg.time.Clock()
width, height = 800, 800

black = (0, 0, 0)
white = (255, 255, 255)
bg_gray = (51, 51, 51)
board_gray = (84, 84, 84)
tile_color = (227, 227, 227)
selected_color = (150, 187, 250)
font = pg.font.Font("OpenSans-Regular.ttf", 50)

screen = pg.display.set_mode((width, height), pg.RESIZABLE)
pg.display.set_caption('Sudoku Solver')

board = h.initial_state()
board_tiles = []
board_back = pg.Rect(0, 0, 0, 0)
selected = None
solving = None
solving_rect = pg.Rect(0, 0, 0, 0)


def solve():
    global board, solving
    game = SudokuGame(board)
    res = game.solve()

    if res:
        board = game.create_board_from_assignment(res)

    solving = None


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

    x_off = 0

    for i in range(len(board)):
        y_off = 0
        tile_row = []
        if i == 3 or i == 6:
            x_off += line_width

        for j in range(len(board)):
            if j == 3 or j == 6:
                y_off += line_width

            col = tile_color
            if selected == (i, j):
                col = selected_color

            tile = h.Tile(board_back.left+(tile_dim*i)+x_off, board_back.top+(tile_dim*j)+y_off, tile_dim, board[i][j],
                          col)
            tile.draw(screen)
            tile_row.append(tile)

        board_tiles.append(tile_row)


def draw_loading(col):
    global solving_rect
    dim = min(width, height)
    solving_rect = pg.Rect(0, 0, dim//3, dim//7)
    solving_rect.center = (width // 2, height // 2)

    pg.draw.rect(screen, col, solving_rect)

    text = font.render('Solving...', True, [255-o for o in col])
    text_rect = text.get_rect()
    text_rect.center = solving_rect.center
    screen.blit(text, text_rect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not solving:
            if not board_back.collidepoint(event.pos):
                selected = None
            else:
                for x in range(len(board_tiles)):
                    for y in range(len(board_tiles)):
                        if board_tiles[x][y].rect.collidepoint(event.pos):
                            selected = (x, y)

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and solving:
            if solving_rect.collidepoint(event.pos):
                solving = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and not solving:
            solve_thread = threading.Thread(target=solve)
            solve_thread.start()

            solving = (0, 0, 0)

        if selected and event.type == pg.KEYDOWN and not solving:
            num = int(event.key)-pg.K_0
            if 0 <= num < 10:
                board[selected[0]][selected[1]] = num

            if int(event.key) == pg.K_KP0:
                board[selected[0]][selected[1]] = 0
            num = int(event.key)-pg.K_KP1+1
            if 1 <= num < 10:
                board[selected[0]][selected[1]] = num

    width, height = screen.get_size()
    screen.fill(bg_gray)
    draw_board()

    if solving:
        draw_loading(solving)

    clock.tick(60)
    pg.display.flip()
