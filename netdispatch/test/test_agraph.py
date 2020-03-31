__author__ = 'Giulio Rossetti'
__license__ = "BSD-Clause-2"
__email__ = "giulio.rossetti@gmail.com"


import unittest
import networkx as nx
try:
    import igraph as ig
except ModuleNotFoundError:
    ig = None

from netdispatch import AGraph


def from_nx_to_igraph(g, directed=False):
    """

    :param g:
    :param directed:
    :return:
    """
    if ig is not None:
        gi = ig.Graph(directed=directed)
        gi.add_vertices(list(g.nodes()))
        gi.add_edges(list(g.edges()))
        return gi


class AGTest(unittest.TestCase):

    def test_neighbors(self):
        g = nx.karate_club_graph()
        ag = AGraph(g)
        n1 = ag.neighbors(1)

        g = from_nx_to_igraph(g)
        ag = AGraph(g)
        n2 = ag.neighbors(1)
        self.assertListEqual(n1, n2)

    def test_predecessors(self):
        g = nx.karate_club_graph()
        g1 = nx.to_directed(g)
        ag = AGraph(g1)
        n1 = ag.predecessors(1)

        g = from_nx_to_igraph(g1, directed=True)
        ag = AGraph(g)
        n2 = ag.predecessors(1)
        self.assertListEqual(n1, n2)

    def test_successors(self):
        g = nx.karate_club_graph()
        g1 = nx.to_directed(g)
        ag = AGraph(g1)
        n1 = ag.successors(1)

        g = from_nx_to_igraph(g1, directed=True)
        ag = AGraph(g)
        n2 = ag.successors(1)
        self.assertListEqual(n1, n2)

    def test_add_edges(self):
        g = nx.karate_club_graph()
        ag = AGraph(g)
        n1 = ag.neighbors(1)
        ag.add_edges(1, [5, 6])
        n2 = ag.neighbors(1)
        n1.extend([5, 6])
        self.assertListEqual(n2, n1)

        g = nx.karate_club_graph()
        g = from_nx_to_igraph(g)
        ag = AGraph(g)
        n3 = ag.neighbors(1)
        ag.add_edges(1, [5, 6])
        n4 = ag.neighbors(1)
        n3.extend([5, 6])
        self.assertListEqual(sorted(n3), sorted(n4))

        self.assertListEqual(sorted(n2), sorted(n4))

    def test_remove_edges(self):
        g = nx.karate_club_graph()
        ag = AGraph(g)
        n1 = ag.neighbors(1)
        ag.remove_edges(1, [0, 2])
        n2 = ag.neighbors(1)
        n1 = [n for n in n1 if n not in [0, 2]]
        self.assertListEqual(n2, n1)

        g = nx.karate_club_graph()
        g = from_nx_to_igraph(g)
        ag = AGraph(g)
        n3 = ag.neighbors(1)
        ag.remove_edges(1, [0, 2])
        n4 = ag.neighbors(1)
        n3 = [n for n in n3 if n not in [0, 2]]
        self.assertListEqual(sorted(n3), sorted(n4))

        self.assertListEqual(sorted(n2), sorted(n4))