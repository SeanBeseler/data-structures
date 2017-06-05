"""Tests the functions for the Graph1 data structure"""
import pytest


@pytest.fixture
def graph():
    from graph1 import Graph1
    new_graph = Graph1()
    return new_graph


def test_init_of_graph1(graph):
    assert new_graph.graph == {}


def test_nodes(graph):
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    assert new_graph.nodes() == [1, 34, 6]


def test_edges(graph):
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.edges() == [(1, 6), (1, 34), (34, 6)]


def test_add_node(graph):
    new_graph.add_node(5)
    assert new_graph.nodes == [5]
    new_graph.add_node(56)
    assert new_graph.nodes == [5, 56]
    new_graph.add_node(12)
    assert new_graph.nodes == [5, 56, 12]
    new_graph.add_node(34)
    assert new_graph.nodes == [5, 56, 12, 34]


def test_add_edge(graph):
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.edges() == [(1, 6), (1, 34), (34, 6)]


def test_delete_node(graph):
    new_graph.add_node(5)
    new_graph.add_node(56)
    new_graph.add_node(12)
    new_graph.add_node(34)
    new_graph.del_node(5)
    assert new_graph.nodes == [56, 12, 34]
    new_graph.del_node(12)
    assert new_graph.nodes == [56, 34]
    new_graph.del_node(56)
    assert new_graph.nodes == [34]


def test_delete_edge(graph):
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


def test_has_node(graph):
    new_graph.add_node(5)
    new_graph.add_node(56)
    new_graph.add_node(12)
    new_graph.add_node(34)
    assert new_graph.has_node(5) is True
    assert new_graph.has_node(12) is True
    assert new_graph.has_node(122) is False


def test_has_edge(graph):
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.has_edge((1, 6)) is True
    assert new_graph.has_edge((34, 6)) is True
    assert new_graph.has_edge((1, 5)) is False


def test_neighbors(graph):
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    new_graph.add_edge(1, 6)
    new_graph.add_edge(1, 34)
    new_graph.add_edge(34, 6)
    assert new_graph.neighbors(1) == (6, 34)
    assert new_graph.neighbors(34) == (6)


def test_adjacent(graph):
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
