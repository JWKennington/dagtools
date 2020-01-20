# Analyzing DAGs in Python

The `dagtools` package provides utilities for computing various 
graph-theoretic properties of DAGs (Directed Acyclic Graphs).

## Graph Formats and Conversion
The `dagtools` package is familiar with the below graph formats, and 
can convert between any of them:

- DOT Format
- `networkx.Graph` and related subclasses

The example below shows how to convert a `networkx` Graph into a
DOT formatted string using the `dagtools.convert` module. Note, the inverse operation
is also available, via the `convert.got_to_graph` function.

```python
>>> import networkx                   
>>> from dagtools import convert
>>> g = networkx.MultiGraph()
>>> g.add_nodes_from([1, 2, 3])
>>> g.add_edges_from([(1, 2), (1, 3)], key=0)
>>> print(convert.graph_to_dot(g))
graph  {
1;
2;
3;
1 -- 2  [key=0];
1 -- 3  [key=0];
}
``` 
