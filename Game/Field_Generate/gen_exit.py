from Cell_Types.water import WaterCell
from random import randint, choice


def generate_exit(self):
    n = self.side_length
    under_water = True
    while under_water:
        exit_border = choice([self.rows, self.columns])[randint(0, n - 1)][choice([0, n])]
        for row in self.field:
            for cell in row:
                for side in range(0, 4):
                    if cell.get_border(side) == exit_border and not isinstance(cell, WaterCell):
                        under_water = False
    exit_border.can_go = exit_border.is_exit = True
