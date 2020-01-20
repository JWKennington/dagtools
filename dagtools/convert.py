"""Loading and converting Graphs in different formats

References:
    [1] The DOT Language https://graphviz.gitlab.io/_pages/doc/info/lang.html
"""

import io

import networkx
from networkx.drawing.nx_pydot import write_dot, read_dot


def graph_to_dot(g: networkx.Graph) -> str:
    """Convert a Graph into DOT formatted string

    Args:
        g:
            Graph, a NetworkX Graph

    Returns:
        str, the formatted DOT string
    """
    with io.StringIO() as f:
        write_dot(g, path=f)
        return f.getvalue()


def dot_to_graph(d: str) -> networkx.Graph:
    """Convert a DOT formatted string into a Graph

    Args:
        d:
            str, the DOT formatted string. See [1] for more about
            the DOT language and formatting.

    Returns:
        Graph, the NetworkX Graph
    """
    with io.StringIO(d) as f:
        return read_dot(path=f)
