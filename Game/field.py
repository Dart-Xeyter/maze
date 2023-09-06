from Field_Generate.BFS import is_connected
from Field_Generate.gen_field import generate_empty_field, generate_basic_borders
from Field_Generate.gen_exit import generate_exit
from Field_Generate.gen_river import generate_river
from Field_Generate.gen_tunnel import generate_tunnel
from Field_Generate.spanning_tree import generate_walls
from Cell_Types.water import WaterCell
from random_generator import randint


class Field:
    def __init__(self, side_length, arguments):
        self.side_length = side_length
        river_max_len = arguments.river_max_len if arguments.river_max_len is not None else side_length
        tunnel_max_len = arguments.tunnel_max_len if arguments.tunnel_max_len is not None else side_length
        walls_max_num = arguments.walls_max_num if arguments.walls_max_num is not None else (side_length-1)**2
        while True:
            generate_empty_field(self)
            generate_basic_borders(self)
            generate_river(self, randint(2, river_max_len))
            generate_tunnel(self, randint(1, tunnel_max_len))
            generate_walls(self, randint(0, walls_max_num))
            generate_exit(self)
            if is_connected(self, self.get_river_tip(2)):
                break

    def get_river_tip(self, type):
        for row in self:
            for cell in row:
                if isinstance(cell, WaterCell) and cell.type == type:
                    return cell

    def __str__(self):
        n = self.side_length
        field = [['#']*(2*n+1) for _ in range(2*n+1)]
        for row in range(n):
            for column in range(n+1):
                field[2*row+1][2*column] = str(self.rows[row][column])
        for column in range(n):
            for row in range(n+1):
                field[2*row][2*column+1] = str(self.columns[column][row])
        for row in range(n):
            for column in range(n):
                field[2*row+1][2*column+1] = str(self.field[row][column])
        return '\n'.join(''.join(q for q in row) for row in field)

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self.field[item]
