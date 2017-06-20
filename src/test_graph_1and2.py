"""Tests the functions for the Graph1 data structure"""
import pytest


def test_init_of_graph1():
    """Tests initialization of graph"""
    from graph1 import Graph1
    new_graph = Graph1()
    assert new_graph.graph == {}


def test_nodes():
    """Test for pulling a list of nodes"""
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_node(1)
    new_graph.add_node(34)
    new_graph.add_node(6)
    assert list(new_graph.nodes()) == [1, 34, 6]


def test_edges():
    """Test for pulling list of edges between nodes"""
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
    """Test for adding nodes to graph"""
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
    """Test for adding edges between nodes"""
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
    """Test for deleting nodes"""
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
    """Test for deleting edges between nodes"""
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
    """Test that a certain node is in the graph"""
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
    """Test for finding neighbors of a particular node"""
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
    """Test that there is an edge between two values"""
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


def test_depth_graph2():
    """Test the depth search of graph"""
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_edge(1, 2)
    new_graph.add_edge(1, 3)
    new_graph.add_edge(2, 4)
    new_graph.add_edge(2, 5)
    new_graph.add_edge(3, 6)
    new_graph.add_edge(3, 7)
    new_graph.add_edge(4, 8)
    new_graph.add_edge(4, 9)
    new_graph.add_edge(5, 10)
    new_graph.add_edge(5, 11)
    new_graph.add_edge(6, 12)
    new_graph.add_edge(6, 13)
    new_graph.add_edge(7, 14)
    new_graph.add_edge(7, 15)
    assert new_graph.depth_first_traversal(1) == [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    assert new_graph.depth_first_traversal(2) == [2, 4, 8, 9, 5, 10, 11]
    assert new_graph.depth_first_traversal(3) == [3, 6, 12, 13, 7, 14, 15]


def test_breadth_graph2():
    """Test the breadth search of a graph"""
    from graph1 import Graph1
    new_graph = Graph1()
    new_graph.add_edge(1, 2)
    new_graph.add_edge(1, 3)
    new_graph.add_edge(2, 4)
    new_graph.add_edge(2, 5)
    new_graph.add_edge(3, 6)
    new_graph.add_edge(3, 7)
    new_graph.add_edge(4, 8)
    new_graph.add_edge(4, 9)
    new_graph.add_edge(5, 10)
    new_graph.add_edge(5, 11)
    new_graph.add_edge(6, 12)
    new_graph.add_edge(6, 13)
    new_graph.add_edge(7, 14)
    new_graph.add_edge(7, 15)
    new_graph.add_edge(9, 'x')
    new_graph.add_edge(9, 'y')
    assert new_graph.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x', 'y']
    assert new_graph.breadth_first_traversal(2) == [2, 4, 5, 8, 9, 10, 11, 'x', 'y']
    assert new_graph.breadth_first_traversal(3) == [3, 6, 7, 12, 13, 14, 15]
