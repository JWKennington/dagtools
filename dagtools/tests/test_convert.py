import networkx
import pytest

from dagtools import graph


def clean_multiline(s: str) -> str:
    """Utility function for cleaning whitespace from a multiline string"""
    return '\n'.join([line.strip() for line in s.split('\n') if line.strip()])


def assert_str_equal(x: str, compare: str):
    """Utility function for comparing equivalence between multiline strings, ignoring whitespace"""
    assert clean_multiline(x) == clean_multiline(compare)


class TestGraphConversions:
    @pytest.fixture(scope='class', autouse=True)
    def g(self):
        _g = networkx.MultiGraph()
        _g.add_nodes_from(['1', '2', '3'])
        _g.add_edge('1', '2', key='0')
        _g.add_edge('1', '3', key='0')
        return _g

    @pytest.fixture(scope='class', autouse=True)
    def dot_string(self):
        return 'graph "G" {\n1;\n2;\n3;\n1 -- 2  [key=0];\n1 -- 3  [key=0];}'

    def test_nx_to_dot(self, g):
        dot = graph.graph_to_dot(g)
        assert_str_equal(dot, '''
        graph  {
        1;
        2;
        3;
        1 -- 2  [key=0];
        1 -- 3  [key=0];
        }
        ''')

    def test_dot_to_nx(self, dot_string, g):
        converted_graph = graph.dot_to_graph(dot_string)
        assert g.adj == converted_graph.adj
