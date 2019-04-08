import networkx as nx
import igraph as ig


class AGraph(object):

    def __init__(self, graph):
        self.graph = graph
        self.__check_type()

    def __check_type(self):
        if isinstance(self.graph, nx.Graph):
            self.directed = nx.is_directed(self.graph)
            self.tp = 0
        elif isinstance(self.graph, ig.Graph):
            self.directed = self.graph.is_directed()
            self.tp = 1
        else:
            raise ValueError("Graph model not supported")

    def neighbors(self, node):
        if not self.directed:
            if self.tp == 0:
                return list(self.graph.neighbors(node))
            if self.tp == 1:
                ng = self.graph.neighbors(node)
                return [self.graph.vs[x]['name'] for x in ng]

    def predecessors(self, node):
        if self.directed:
            if self.tp == 0:
                print("here")
                return list(self.graph.predecessors(node))
            if self.tp == 1:
                ng = self.graph.predecessors(node)
                return [self.graph.vs[x]['name'] for x in ng]

    def successors(self, node):
        if self.directed:
            if self.tp == 0:
                return list(self.graph.successors(node))
            if self.tp == 1:
                ng = self.graph.successors(node)
                return [self.graph.vs[x]['name'] for x in ng]