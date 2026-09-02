# __init__.py
#
# The pygrad package initialization file
#
# Usage:
#   import pygrad as pg
#   s = pg.Scalar(value=1.0)
#   import pygrad.viz
#   img = pygrad.viz.draw_graph(s)
#
#   ## OR ##
#
#   from pygrad import *
#   s = Scalar(value=1.0)
#   import pygrad.viz as pgv
#   img = pgv.draw_graph(s)

from .scalar import Scalar
from .trainable import Trainable
from .neuron import Neuron
from .layer import Layer
from .mlp import MLP

__all__ = [
 'Scalar',
 'Neuron',
 'Layer',
 'MLP'
]
