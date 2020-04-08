class GraphUL:
    def __init__(self,V): # Constructor  
        self.V = V        # No. of vertices  
        self.EAdjList  = [[] for i in range(V)]  # adjacency lists  

    def add_edge(self, src, dest):
        if src not in self.EAdjList[dest]:
            self.EAdjList[dest].append(src)
        if dest not in self.EAdjList[src]:
            self.EAdjList[src].append(dest)

    def remove_edge(self, src, dest):
        if src in self.EAdjList[dest]:
            self.EAdjList[dest].pop(src)
        if dest in self.EAdjList[src]:
            self.EAdjList[src].pop(dest)

    def print_graph(self):
        for vertex in range(self.V):
            print(f"\nAdjaceny List For Vertex {vertex} :")
            print('head', end='')
            for v in self.EAdjList[vertex]:
                print(f'--> {v} ', end=' ')


class GraphUM:
    def __init__(self, vertices):
        self.V = vertices
        # size of list = V
        self.EAdjMatrix = [[0]*self.V for j in range(self.V)]

    def add_edge(self, src, dest):
        if src < self.V and dest < self.V:
            self.EAdjMatrix[src][dest] = 1
            self.EAdjMatrix[dest][src] = 1

    def remove_edge(self, src, dest):
        if src < self.V and dest < self.V:
            self.EAdjMatrix[src][dest] = -1
            self.EAdjMatrix[dest][src] = -1

    def print_graph(self):
        print(f"\nAdjaceny Matrix :")
        print(self.EAdjMatrix)


if __name__ == "__main__":
    V = 5
    graph = GraphUM(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # print(graph.EAdjList)
    graph.print_graph()
