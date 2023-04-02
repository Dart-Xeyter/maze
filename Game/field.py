from border import Border
from cell import *
from random_generator import *


class Field:
    def __init__(self, side_length):
        self.side_length = side_length
        self.field = [[] for _ in range(side_length)]
        self.rows = [[] for _ in range(side_length)]
        self.columns = [[] for _ in range(side_length)]
        for i in range(side_length):
            for j in range(side_length+1):
                self.rows[i].append(Border(0 < j < side_length, False))
                self.columns[i].append(Border(0 < j < side_length, False))
        exit_border = choice([self.rows, self.columns])[randint(0, side_length-1)][choice([0, side_length])]
        exit_border.can_go = exit_border.is_exit = True
        for i in range(side_length):
            for j in range(side_length):
                self.field[i].append(EmptyCell(i, j, self))
        # нагенерить стенки внутри

    def __getitem__(self, item):
        return self.field[item]
