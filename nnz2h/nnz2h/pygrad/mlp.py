# mlp.py
#
# Contains a Python class called "MLP" with a list of neuron Layer objects

# import Python modules
from .trainable import Trainable
from .layer import Layer

# MLP class is trainable
class MLP(Trainable):
  """
  Represents a multi-layer perceptron (MLP)
  """
  def __init__(self, num_i, num_os:list[int], activation:str=None):
    """
    MLP constructor
    """
    # create a list of layer num_is
    num_is = [num_i]+num_os
    # public variables
    self.layers = [\
     Layer(num_is[i],num_is[i+1],activation=activation)\
     for i in range(0,len(num_is)-1)\
    ]

  def __call__(self, x):
    """
    Callable instance of MLP object
    """
    for layer in self.layers:
      x = layer(x)
    return x

  def parameters(self):
    return [p for layer in self.layers for p in layer.parameters()]

  def __repr__(self):
    """
    MLP string representation for pretty-printing
    """
    return f"MLP({', '.join(str(layer) for layer in self.layers)})"
