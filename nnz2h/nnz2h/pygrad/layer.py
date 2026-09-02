# layer.py
#
# Contains a Python class called "Layer" with a list of Neuron objects

# import Python modules
from .trainable import Trainable
from .neuron import Neuron

# Neuron class is trainable
class Layer(Trainable):
  """
  Represents a layer of neurons
  """
  def __init__(self, num_i, num_o, **kwargs):
    """
    Layer constructor
    """
    # public variables
    self.neurons = [Neuron(num_i, **kwargs) for i in range(0,num_o)]

  def __call__(self, x):
    """
    Callable instance of Layer object
    """
    out = [n(x) for n in self.neurons]
    return out[0] if len(out)==1 else out

  def parameters(self):
    return [p for n in self.neurons for p in n.parameters()]

  def __repr__(self):
    """
    Neuron string representation for pretty-printing
    """
    return f"Layer({', '.join(str(n) for n in self.neurons)})"
