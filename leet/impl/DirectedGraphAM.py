class DirectedGraphAM:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, w=1):
        """Adds an edge (u,v) with weight w"""
        # Create dict associated with source vertex
        if u not in self.edges:
            self.edges[u] = {}
        if v not in self.edges:
            self.edges[v] = {}
        # Set weight
        self.edges[u][v] = w

    def __iter__(self):
        for u in self.edges:
            yield str(u)

    def __repr__(self):
        return "Edges: " + " ; ".join([str([u, self.edges[u]]) for u in self.edges])


if __name__ == '__main__':
    g1 = DirectedGraphAM()
    g1.add_edge('a', 'b')
    g1.add_edge('c', 'b')
    g1.add_edge('c', 'a')
    print("Vertices: " + ",".join(g1))
    print(g1)
