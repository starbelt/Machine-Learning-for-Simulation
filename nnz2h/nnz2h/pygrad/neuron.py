# neuron.py
#
# Contains a Python class called "Neuron" with a vector of Scalar weight
# parameters and a Scalar bias parameter

# import Python modules
import random # random.uniform
from .scalar import Scalar
from .trainable import Trainable

# Neuron class is trainable
class Neuron(Trainable):
  """
  Represents a single neuron with a vector of Scalar weight parameters and a
  Scalar bias parameter. Activation string options: None, 'tanh', 'relu'
  """
  def __init__(self, num_i, activation:str=None):
    """
    Neuron constructor
    """
    # public variables
    ## weights: a list of Scalar objects randomly initialized
    self.w = [Scalar(random.uniform(-1.0,1.0)) for i in range(0,num_i)]
    ## bias: a Scalar object initialized to zero
    self.b = Scalar(0.0)

    # public instance functions
    ## set the activation function
    self.act = lambda: None
    self.act.__name__ = 'None'
    if activation:
      self.act = getattr(Scalar,activation)

  def __call__(self, x):
    """
    Callable instance of Neuron object
    """
    out = sum((wi*xi for wi,xi in zip(self.w,x)),self.b)
    return self.act(out) if self.act.__name__!='None' else out

  def parameters(self):
    return self.w+[self.b]

  def __repr__(self):
    """
    Neuron string representation for pretty-printing
    """
    return f"Neuron(num_i={len(self.w)},act={self.act.__name__})"
