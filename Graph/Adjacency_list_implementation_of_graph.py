""" Adjacency list implementation of graph. """

class Graph:
    def __init__(self, vertex_count=0) -> None:
        self.vertex_count = vertex_count
        self.adj_list = {f"V{i}": [] for i in range(vertex_count)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[f"V{u}"].append((v, weight))
            self.adj_list[f"V{v}"].append((u, weight))
        else:
            print("Invalid Vertex.")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[f"V{u}"] = [(vertex, weight) for vertex, weight in self.adj_list[f"V{u}"] if vertex != v]
            self.adj_list[f"V{v}"] = [(vertex, weight) for vertex, weight in self.adj_list[f"V{v}"] if vertex != u]
        else:
            print("Invalid Vertex.")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            if self.adj_list[f"V{u}"]:
                return any(vertex == v for vertex, _ in self.adj_list[f"V{u}"])
        print("invalid vertex has_edge.")
        return False

    def print_adj_list(self):
        for vertex, value in self.adj_list.items():
            print(vertex, ":", value)

graph = Graph(vertex_count=5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

graph.print_adj_list()
print(graph.has_edge(3, 4))
graph.remove_edge(3, 4)
print(graph.has_edge(3, 4))
graph.print_adj_list()
