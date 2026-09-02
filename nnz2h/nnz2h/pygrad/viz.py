# viz.py
#
# Contains functions for visualizing a function as a graph

# import Python modules
from graphviz import Digraph

# a function to build a graph given the sink (snk) node
def make_graph(snk):
  nodes, edges = set(), set()
  def _recursive_build(v):
    if v not in nodes:
      nodes.add(v)
      for src in v._srcs:
        edges.add((src,v))
        _recursive_build(src)
  _recursive_build(snk)
  return nodes, edges

def draw_graph(snk):
  # LR sets the visualization to read from left to right
  g = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
  nodes, edges = make_graph(snk)
  for n in nodes:
    uid = str(id(n))
    # for each node, create a rectangular ('record')
    g.node(\
     name=uid,\
     label="{%s | value %.4f | grad %.4f}" % (n._id, n.value, n.grad),\
     shape='record'\
    )
    # create and op node if the value node is the result of an operation
    if n._op!='':
      g.node(name=uid+n._op, label=n._op)
      g.edge(uid+n._op, uid)
  # draw missing edges for op nodes
  for n1, n2 in edges:
     g.edge(str(id(n1)),str(id(n2))+n2._op)
  return g
