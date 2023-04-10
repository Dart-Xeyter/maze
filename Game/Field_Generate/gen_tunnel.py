from random_generator import get_random_cell
from Cell_Types.hole import HoleCell


def generate_tunnel(self, length):
    tunnel = []
    for q in range(length):
        cell = get_random_cell(self)
        cell = HoleCell(cell.row_index, cell.column_index, self, q+1)
        self.field[cell.row_index][cell.column_index] = cell
        tunnel.append(cell)
    for i in range(length):
        tunnel[i].next = tunnel[(i + 1) % length]
