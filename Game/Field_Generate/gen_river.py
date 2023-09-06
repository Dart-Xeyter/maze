from random_generator import get_random_cell, get_random_neighbour
from Cell_Types.water import WaterCell


def generate_river(self, max_len):
    river = [get_random_cell(self)]
    for i in range(1, max_len+1):
        cell = WaterCell(river[-1].row_index, river[-1].column_index, self, 2)
        river[-1] = self.field[cell.row_index][cell.column_index] = cell
        following = get_random_neighbour(cell)
        if i == max_len or following is None:
            break
        river.append(following)
    for q in range(len(river)-1):
        river[q].next, river[q].type = river[q+1], q > 0
