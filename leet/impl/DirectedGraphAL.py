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

    def neighbors(self, u):
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield e

    def __repr__(self):
        rep = 'grh:['
        for v in range(self.size):
            for e in self.neighbors(v):
                rep += str(v) + '->' + str(e) + ', '
        rep += ']'
        return rep