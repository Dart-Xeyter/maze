from random_generator import get_random_cell, get_random_neighbour
from Cell_Types.water import WaterCell


def generate_river(self, max_len):
    cell = get_random_cell(self)
    cell = WaterCell(cell.row_index, cell.column_index, self, 0)
    self.field[cell.row_index][cell.column_index] = cell
    for i in range(1, max_len + 1):
        following_side = get_random_neighbour(cell)
        if following_side is None or i == max_len:
            cell = WaterCell(cell.row_index, cell.column_index, self, 2)
            self.field[cell.row_index][cell.column_index] = cell
            break
        following = cell.get_neighbour(following_side)
        following = WaterCell(following.row_index, following.column_index, self, 1)
        self.field[following.row_index][following.column_index] = following
        cell.next, cell = following_side, following
