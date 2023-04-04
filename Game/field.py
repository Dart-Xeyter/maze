from border import Border
from random_generator import *
from Cell_Types.water import WaterCell
from Cell_Types.hole import HoleCell


class Field:
    river_name, tunnel_name = 'river_max_len', 'tunnel_max_len'

    def __init__(self, side_length, **kwargs):
        self.side_length = side_length
        self.generate_empty_field()
        self.generate_basic_borders()
        exit_border = choice([self.rows, self.columns])[randint(0, side_length-1)][choice([0, side_length])]
        exit_border.can_go = exit_border.is_exit = True
        river_max_len = kwargs[Field.river_name] if Field.river_name in kwargs else side_length
        self.generate_river(randint(2, river_max_len))
        tunnel_max_len = kwargs[Field.tunnel_name] if Field.tunnel_name in kwargs else side_length
        self.generate_tunnel(randint(1, tunnel_max_len))

    def generate_empty_field(self):
        n = self.side_length
        self.field = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.field[i].append(LandCell(i, j, self))

    def generate_basic_borders(self):
        n = self.side_length
        self.rows = [[] for _ in range(n)]
        self.columns = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n + 1):
                self.rows[i].append(Border(0 < j < n, False))
                self.columns[i].append(Border(0 < j < n, False))

    def generate_river(self, max_len):
        cell = get_random_cell(self)
        cell = WaterCell(cell.row_index, cell.column_index, self, 0)
        self.field[cell.row_index][cell.column_index] = cell
        for i in range(1, max_len+1):
            following_side = get_random_neighbour(cell)
            if following_side is None or i == max_len:
                cell = WaterCell(cell.row_index, cell.column_index, self, 2)
                self.field[cell.row_index][cell.column_index] = cell
                break
            following = cell.get_neighbour(following_side)
            following = WaterCell(following.row_index, following.column_index, self, 1)
            self.field[following.row_index][following.column_index] = following
            cell.next, cell = following_side, following

    def generate_tunnel(self, length):
        tunnel = []
        for _ in range(length):
            cell = get_random_cell(self)
            cell = HoleCell(cell.row_index, cell.column_index, self)
            self.field[cell.row_index][cell.column_index] = cell
            tunnel.append(cell)
        for i in range(length):
            tunnel[i].next = tunnel[(i+1) % length]

    def __getitem__(self, item):
        return self.field[item]
