""" Adjacency matrix implementation of graph """

class Graph:
    def __init__(self, vertex_count=None) -> None:
        self.vertex_count = vertex_count
        self.adj_matrix = [[0]*vertex_count for i in range(vertex_count)]

    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("invalid vertex.")

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("invalid vertex.")


    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] or self.adj_matrix[v][u]
        return False

    def print_adj_matrix(self):
        for row_value in self.adj_matrix:
            row_list = " ".join(map(str, row_value))
            print(row_list)


graph = Graph(vertex_count=5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

graph.print_adj_matrix()
print(graph.has_edge(3, 4))
graph.remove_edge(3, 4)
print(graph.has_edge(3, 4))
graph.print_adj_matrix()


