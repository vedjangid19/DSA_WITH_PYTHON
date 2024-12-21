"""Bredth first search implementation in graph using queue data structure."""

class Queue:
    def __init__(self) -> None:
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0
    
    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        
        if not self.is_empty():
            return self.list.pop(0)
        else:
            raise IndexError("Queue is empty.")
        
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Queue is empty.")


class Graph:
    def __init__(self, vertex_count=None) -> None:
        self.vertex_count = vertex_count
        self.queue = Queue()
        self.graph = {i: [] for i in range(vertex_count)}
        self.output_list = []

    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.graph[u].append((v, weight))
            self.graph[v].append((u, weight))
        else:
            print("Invalid vertex.")

    def BFS(self, source=0):

        visited_list = [False]*self.vertex_count

        self.queue.enqueue(data=source)
        visited_list[source] = True
        
        while not self.queue.is_empty():
            temp = self.queue.dequeue()
            
            self.output_list.append(temp)

            for vertex, _ in self.graph[temp]:
                if not visited_list[vertex]:
                    self.queue.enqueue(data=vertex)

                    visited_list[vertex] = True

        return " ".join(map(str, (self.output_list)))


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

    print(graph.BFS())

