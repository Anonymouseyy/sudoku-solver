import pygame as pg

pg.init()
value_font = pg.font.Font("OpenSans-Regular.ttf", 50)


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


def to_group_major(board):
    """
    :param board: A row-major Sudoku board
    :return: Group major board with 0, 1, 2
                                    3, 4, 5
                                    6, 7, 8 order for each group and the whole board
    """

    gm_board = []
    x_off = 0
    y_off = 0

    for i in range(len(board)):
        tile_cell = []

        for j in range(len(board)):
            tile_cell.append(board[(j//3)+x_off*3][(j % 3)+y_off*3])

        gm_board.append(tile_cell)
        x_off += 1

        if x_off % 3 == 0:
            x_off = 0
            y_off += 1

    return gm_board


def to_column_major(board):
    return [[row[i] for row in board] for i in range(len(board))]


def check_validity(board):
    """
    :param board: Row major board
    :return: True if board is valid, false if not
    """
    # Needs to account for 0s
    return not (any([len([x for x in row if x != 0]) != len(set([x for x in row if x != 0])) for row in board]) or
                any([len([x for x in col if x != 0]) != len(set([x for x in col if x != 0]))
                     for col in to_column_major(board)]) or
                any([len([x for x in group if x != 0]) != len(set([x for x in group if x != 0]))
                                                                 for group in to_group_major(board)]))
