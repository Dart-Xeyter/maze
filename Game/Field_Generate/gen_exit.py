from Cell_Types.water import WaterCell
from random import randint, choice


def generate_exit(self):
    n = self.side_length
    under_water = True
    while under_water:
        exit_border = choice([self.rows, self.columns])[randint(0, n - 1)][choice([0, n])]
        exit_cell = next((cell for cell in row
                          if any(self.get_border(side) == exit_border for side in range(4)))
                         for row in self.field)
        under_water = isinstance(exit_cell, WaterCell)
    exit_border.can_go = exit_border.is_exit = True
