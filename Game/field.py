from Field_Generate.BFS import is_connected
from Field_Generate.gen_field import generate_empty_field, generate_basic_borders
from Field_Generate.gen_exit import generate_exit
from Field_Generate.gen_river import generate_river
from Field_Generate.gen_tunnel import generate_tunnel
from Field_Generate.spanning_tree import generate_walls
from Cell_Types.water import WaterCell
from random_generator import randint


class Field:
    river_name, tunnel_name, wall_name = 'river_max_len', 'tunnel_max_len', 'wall_max_num'

    def __init__(self, side_length, **kwargs):
        self.side_length = side_length
        while True:
            generate_empty_field(self)
            generate_basic_borders(self)
            river_max_len = kwargs[Field.river_name] if Field.river_name in kwargs else side_length
            generate_river(self, randint(2, river_max_len))
            tunnel_max_len = kwargs[Field.tunnel_name] if Field.tunnel_name in kwargs else side_length
            generate_tunnel(self, randint(1, tunnel_max_len))
            walls_max_num = kwargs[Field.wall_name] if Field.wall_name in kwargs else (side_length-1)**2
            generate_walls(self, randint(0, walls_max_num))
            generate_exit(self)
            if is_connected(self, self.get_mouth()):
                break

    def get_mouth(self):
        for row in self:
            for cell in row:
                if isinstance(cell, WaterCell) and cell.type == 2:
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
