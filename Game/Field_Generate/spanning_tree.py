from Field_Generate.DSU import DSU
from Cell_Types.water import WaterCell
from Cell_Types.hole import HoleCell
from random_generator import shuffled


class Edge:
    def __init__(self, first, second, under_water):
        self.first, self.second = first, second
        self.under_water = under_water

    def build_wall(self):
        self.first.get_border(1+(self.first.row_index == self.second.row_index)).can_go = False


def generate_edge(first, second):
    under_water = isinstance(first, WaterCell) and isinstance(second, WaterCell)
    return Edge(first, second, under_water)


def generate_walls(field, max_num):
    n = field.side_length
    edges = []
    for q in range(n):
        for q1 in range(n-1):
            edges.append(generate_edge(field[q][q1], field[q][q1+1]))
            edges.append(generate_edge(field[q1][q], field[q1+1][q]))
    dsu = DSU(n*n)
    for edge in edges:
        if edge.under_water:
            dsu.merge(edge.first, edge.second)
    for row in field:
        for cell in row:
            if isinstance(cell, HoleCell):
                dsu.merge(cell, cell.next)
    edges = shuffled([edge for edge in edges if not edge.under_water])
    number_walls = 0
    for edge in edges:
        if not dsu.merge(edge.first, edge.second) and number_walls < max_num:
            edge.build_wall()
            number_walls += 1
