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

    @property
    def nodes(self):
        if self.tp == 0:
            return self.graph.nodes()
        elif self.tp == 1:
            return self.graph.vs['name']
        else:
            raise ValueError("Graph model not supported")

    @property
    def edges(self):
        if self.tp == 0:
            return self.graph.edges()
        elif self.tp == 1:
            return [(self.graph.vs[e.tuple[0]]['name'], self.graph.vs[e.tuple[1]]['name']) for e in self.graph.es]
        else:
            raise ValueError("Graph model not supported")

    def number_of_nodes(self):
        if self.tp == 0:
            return self.graph.number_of_nodes()
        elif self.tp == 1:
            return len([self.graph.vs])
        else:
            raise ValueError("Graph model not supported")

    def neighbors(self, node):
        if not self.directed:
            if self.tp == 0:
                return list(self.graph.neighbors(node))
            if self.tp == 1:
                ng = self.graph.neighbors(node)
                return [self.graph.vs[x]['name'] for x in ng]
        else:
            return self.successors(node)

    def predecessors(self, node):
        if self.directed:
            if self.tp == 0:
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

    def get_edge_attributes(self, attribute):
        if self.tp == 0:
            return nx.get_edge_attributes(self.graph, attribute)
        if self.tp == 1:
            ea = self.graph.es[attribute]
            res = {(self.graph.vs[e.tuple[0]]['name'], self.graph.vs[e.tuple[1]]['name']): ea[attribute] for e in ea}
            return res

    def get_node_attributes(self, attribute):
        if self.tp == 0:
            return nx.get_node_attributes(self.graph, attribute)
        if self.tp == 1:
            nodes = self.graph.vs[attribute]
            res = {self.graph.vs[x]['name']: x[attribute] for x in nodes}
            return res
