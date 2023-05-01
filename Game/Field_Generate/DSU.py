class DisjointSetUnion:
    def __init__(self, size):
        self.sizes = [1]*size
        self.parent = [q for q in range(size)]

    @staticmethod
    def get_number(vertex):
        return vertex.row_index*vertex.field.side_length+vertex.column_index

    def get_root(self, vertex):
        vertex = DisjointSetUnion.get_number(vertex)
        path = []
        while self.parent[vertex] != vertex:
            path.append(vertex)
            vertex = self.parent[vertex]
        for node in path:
            self.parent[node] = vertex
        return vertex

    def merge(self, first, second):
        first, second = self.get_root(first), self.get_root(second)
        if first == second:
            return False
        if self.sizes[first] < self.sizes[second]:
            first, second = second, first
        self.sizes[first] += self.sizes[second]
        self.parent[second] = first
        return True

    def merge_next(self, cell):
        try:
            self.merge(cell, cell.next)
        except AttributeError:
            pass
