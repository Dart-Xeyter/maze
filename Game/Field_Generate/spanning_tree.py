from Field_Generate.DSU import DisjointSetUnion
from Cell_Types.water import WaterCell
from Cell_Types.cell import Cell
from random_generator import shuffled


class Edge:
    def __init__(self, first_vertex: Cell, second_vertex: Cell):
        self.first_vertex, self.second_vertex = first_vertex, second_vertex

    def build_wall(self):
        self.first_vertex.get_border(1+(self.first_vertex.row_index != self.second_vertex.row_index)).can_go = False


def add_edge(first_vertex: Cell, second_vertex: Cell, edges):
    under_river = isinstance(first_vertex, WaterCell) and first_vertex.next == second_vertex or \
                  isinstance(second_vertex, WaterCell) and second_vertex.next == first_vertex
    if not under_river:
        edges.append(Edge(first_vertex, second_vertex))


def generate_walls(field, max_num):
    n = field.side_length
    edges = []
    for first_index in range(n):
        for second_index in range(n-1):
            add_edge(field[first_index][second_index], field[first_index][second_index+1], edges)
            add_edge(field[second_index][first_index], field[second_index+1][first_index], edges)
    edges = shuffled(edges)
    dsu = DisjointSetUnion(n*n)
    for row in field:
        for cell in row:
            dsu.merge_next(cell)
    number_walls = 0
    for edge in edges:
        if number_walls < max_num and not dsu.merge(edge.first_vertex, edge.second_vertex):
            edge.build_wall()
            number_walls += 1
