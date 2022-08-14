######### Directed Weighted Graph and Search ############
class Graph:
    def __init__(self, nodes=None, edges=None):

        self.nodes, self.adj = [], {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, x):
        return x in self.nodes

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, x):
        return iter(self.adj[x])

    def __str__(self):
        return 'V: %s\nE: %s' % (self.nodes, self.adj)

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.adj[n] = []

    def add_nodes_from(self, i):
        for n in i:
            self.add_node(n)

    def add_edge(self, u, v):  # undirected unweighted graph
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]

    def add_edges_from(self, i):
        for n in i:
            self.add_edge(*n)

    def number_of_nodes(self):

        return len(self.nodes)

    def number_of_edges(self):

        return sum(len(l) for _, l in self.adj.items()) // 2


class DGraph(Graph):
    def add_edge(self, u, v):

        self.adj[u] = self.adj.get(u, []) + [v]


class WGraph(Graph):
    def __init__(self, nodes=None, edges=None):

        self.nodes, self.adj, self.weight = [], {}, {}
        if nodes != None:
            self.add_nodes_from(nodes)
        if edges != None:
            self.add_edges_from(edges)

    def add_edge(self, u, v, w):
        self.adj[u] = self.adj.get(u, []) + [v]
        self.adj[v] = self.adj.get(v, []) + [u]
        self.weight[(u, v)] = w
        self.weight[(v, u)] = w

    def get_weight(self, u, v):

        return self.weight[(u, v)]


class DWGraph(WGraph):
    def add_edge(self, u, v, w):

        self.adj[u] = self.adj.get(u, []) + [v]
        self.weight[(u, v)] = w


if __name__ == '__main__':
    pass
