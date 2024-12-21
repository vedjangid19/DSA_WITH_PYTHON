"""Depth first search implementation in graph using stack data structure."""

class Stack:
    def __init__(self) -> None:
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Stack is empty.")


class Graph:
    def __init__(self, vertex_count=0) -> None:
        self.vertex_count = vertex_count
        self.stack = Stack()
        self.output = []
        self.graph = {i : [] for i in range(self.vertex_count)}

    def add_edge(self, u, v, weight=1):
        if u<=self.vertex_count and v<=self.vertex_count:
            self.graph[u].append((v, weight))
            self.graph[v].append((u, weight))
        else:
            print("vertex invalid.")
        
    def DFS(self, source=0):

        visited_list = [False]*self.vertex_count
        
        self.stack.push(source)
        visited_list[source] = True

        while not self.stack.is_empty():
            temp = self.stack.pop()
            self.output.append(temp)

            for vertex, _ in self.graph[temp]:
                if not visited_list[vertex]:
                    self.stack.push(vertex)

                    visited_list[vertex] = True
        
        return " ".join(map(str, self.output))


if __name__ == "__main__":

    graph = Graph(vertex_count=6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    print(graph.DFS())
