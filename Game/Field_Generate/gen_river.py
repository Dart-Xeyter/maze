from random_generator import get_random_cell, get_random_neighbour
from Cell_Types.water import WaterCell


def generate_river(self, max_len):
    river = [get_random_cell(self)]
    for i in range(1, max_len):
        following = get_random_neighbour(river[-1])
        if following is None:
            break
        river.append(following)
    assert len(river) > 1
    for index, cell in enumerate(river):
        cell = WaterCell(cell.row_index, cell.column_index, self, (index != 0)+(index == len(river)-1))
        river[index] = self.field[cell.row_index][cell.column_index] = cell
    for q in range(len(river)-1):
        river[q].next = river[q+1]
