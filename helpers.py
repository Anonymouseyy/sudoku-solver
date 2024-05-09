class tile:
    def __init__(self, x=0, y=0, d=0, value=0):
        self.x = x
        self.y = y
        self.d = d
        self.value = value


def initial_state():
    return [[0 for _ in range(9)] for _ in range(9)]
