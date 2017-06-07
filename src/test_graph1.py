"""Tests the functions for the Graph1 data structure"""
import pytest



def test_init_of_graph1():
    from graph1 import Graph1
    new_graph = Graph1()
    assert new_graph.graph == {}


def test_nodes():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    assert list(new_graph.nodes()) == [1, 34, 6]


def test_edges():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.edges() == [(1, 6), (1, 34), (34, 6)]


def test_add_node():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(5)
    assert new_graph.nodes() == [5]
    new_graph.add_node(56)
    assert 56 in new_graph.nodes()
    new_graph.add_node(12)
    assert 12 in new_graph.nodes()
    new_graph.add_node(34)
    assert 34 in new_graph.nodes()


def test_add_edge():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.edges() == [(1, 6), (1, 34), (34, 6)]


def test_delete_node():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(5)
    new_graph.add_node(56)
    new_graph.add_node(12)
    new_graph.add_node(34)
    new_graph.del_node(5)
    assert 5 not in new_graph.nodes()
    new_graph.del_node(12)
    assert 12 not in new_graph.nodes()
    new_graph.del_node(56)
    assert 56 not in new_graph.nodes()


def test_delete_edge():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    new_graph.del_edge(1, 6)
    assert new_graph.edges() == [(1, 34), (34, 6)]
    new_graph.del_edge(34, 6)
    assert new_graph.edges() == [(1, 34)]


def test_has_node():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(5)
    new_graph.add_node(56)
    new_graph.add_node(12)
    new_graph.add_node(34)
    assert new_graph.has_node(5) is True
    assert new_graph.has_node(12) is True
    assert new_graph.has_node(122) is False



def test_neighbors():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.neighbors(1) == [6, 34]
    assert new_graph.neighbors(34) == [6]


def test_adjacent():
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_node(45)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.adjacent(1, 6) is True
    assert new_graph.adjacent(1, 34) is True
    assert new_graph.adjacent(45, 1) is False
