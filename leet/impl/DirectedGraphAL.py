class DirectedGraphAL:
    def __init__(self, size):
        self.vertices = [None] * size
        self.size = size

    def add_edge(self, u, v, w=1):
        """Adds an edge (u,v) with weight w"""
        # Create an adjacency list to store all edges emanating from vertex u
        if self.vertices[u] is None:
            self.vertices[u] = []
        # Following logic is needed for adding same edge with different weight
        for e in self.vertices[u]:
            if e[0] == v:
                print("Removing an existing edge {} from {}".format(e, u))
                self.vertices[u].remove(e)
                break
        # Add edge info with weight.
        self.vertices[u].append((v, w))

    def edges(self, u):
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield e

    def __iter__(self):
        for i in range(len(self.vertices)):
            yield i

    def __repr__(self):
        return "Edges: " + " ; ".join([str([i, self.vertices[i]]) for i in range(len(self.vertices))])


if __name__ == '__main__':
    g1 = DirectedGraphAL(3)
    g1.add_edge(0, 1)
    g1.add_edge(2, 1)
    g1.add_edge(2, 0)
    print("Vertices: " + ",".join([str(i) for i in g1]))
    print("Edges of vertex 2: ")
    for (v, w) in g1.edges(2):
        print("  2 -- [" + str(w) + "] --> " + str(v))
