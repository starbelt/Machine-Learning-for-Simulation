# scalar.py
#
# Contains a Python class called "Scalar" for representing scalars in function
# graphs that can be trained/tuned using gradients.

# import Python modules
import math # exp

# Scalar class
class Scalar:
  """
  Represents scalars in functions. When a function is represented as a graph of
  Scalar objects, it can be tuned using back-propagated gradients.
  """
  def __init__(self, value, _srcs=(), _op='', _id=''):
    """
    Scalar constructor
    """
    # public variables
    ## the scalar value of the object
    self.value = value
    ## a variable for accumulating gradients (to be set later)
    self.grad  = 0.0

    # private variables
    ## store the tuple of source scalars as a set
    self._srcs = set(_srcs)
    ## a string to indicate the operation that creates the scalar
    ## for visualization and debugging purposes
    self._op = _op
    ## a string to identify and label the scalar
    ## for visualization and debugging purposes
    self._id = _id

    # private instance functions
    ## for accumulating gradients (to be set later)
    self._acc_grads = lambda: None

  def __repr__(self):
    """
    Scalar string representation for pretty-printing
    """
    return f"Scalar(value={self.value:.6f},grad={self.grad:.6f})"

  def __add__(self, other):
    """
    self+other
    """
    if not isinstance(other, Scalar):
      other = Scalar(other,_id=str(other))
    out = Scalar(\
     self.value+other.value,_srcs=(self,other),_op='+',\
     _id=self._id+'+'+str(other.value)\
    )
    # define gradient accumulation
    def _acc_grads():
      self.grad += out.grad
      other.grad += out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  def __mul__(self, other):
    """
    self*other
    """
    if not isinstance(other, Scalar):
      other = Scalar(other,_id=str(other))
    out = Scalar(\
     self.value*other.value,_srcs=(self,other),_op='*',\
     _id=self._id+'*'+str(other.value)\
    )
    # define gradient accumulation
    def _acc_grads():
      self.grad += other.value*out.grad
      other.grad += self.value*out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  def __pow__(self, other):
    """
    self**p where p is an integer or floating point number
    """
    assert isinstance(other, (int, float)), 'only supporting int/float powers'
    out = Scalar(\
     self.value**other,_srcs=(self,),_op=f"^{other}",\
     _id=self._id+'^'+str(other)\
    )
    # define gradient accumulation
    def _acc_grads():
      self.grad += (other*self.value**(other-1.0))*out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  def __rpow__(self, other):
    """
    b**self where b is an integer or floating point number
    """
    assert isinstance(other, (int, float)), 'only supporting int/float powers'
    assert other>0, 'only supporting positive base constants'
    out = Scalar(\
     other**self.value,_srcs=(self,),_op=f"{other}^",\
     _id=self._id+'^'+str(other)\
    )
    # define gradient accumulation
    def _acc_grads():
      self.grad += out.value*math.log(other)*out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  def __neg__(self):
    """
    -self can be rewritten as self*-1
    """
    return self*-1

  def __radd__(self, other):
    """
    other+self can be rewritten as self+other
    """
    return self+other

  def __sub__(self, other):
    """
    self-other can be rewritten as self+(-other)
    """
    return self+(-other)

  def __rsub__(self, other):
    """
    other-self can be rewritten as other+(-self)
    """
    return other+(-self)

  def __rmul__(self, other):
    """
    other*self can be rewritten as self*other
    """
    return self*other

  def __truediv__(self, other):
    """
    self/other can be rewritten as self*other**-1
    """
    return self*other**-1

  def __rtruediv__(self, other):
    """
    other/self can be rewritten as other*self**-1
    """
    return other*self**-1

  @staticmethod
  def tanh(s):
    """
    Activation function (saturating): hyperbolic tangent
    """
    # calculate intermediate value for reuse
    e2v = math.exp(2*s.value)
    # a closed-form expression equivalent to hyperbolic tangent:
    # tanh(x) = (e^(2x)-1)/(e^(2x)+1)
    v = (e2v-1.0)/(e2v+1.0)
    out = Scalar(v,_srcs=(s,),_op='tanh')
    # define gradient accumulation
    def _acc_grads():
      s.grad += (1.0-v**2.0)*out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  @staticmethod
  def relu(s):
    """
    Activation function (non-saturating): rectified linear unit
    """
    out = Scalar(0 if s.value<0 else s.value,_srcs=(s,),_op='ReLU')
    # define gradient accumulation
    def _acc_grads():
      s.grad += (out.value>0)*out.grad
    # set gradient accumulation function of output
    out._acc_grads = _acc_grads
    # return the output
    return out

  ## other activation functions: sigmoid (saturating), leaky ReLU (non), gelu

  def acc_grads(self):
    """
    Accumulate gradients
    """
    # construct a topological ordering of scalars in the function graph
    topo = []
    visited = set()
    def build_topo(v):
      if v not in visited:
        visited.add(v)
        for src in v._srcs:
          build_topo(src)
        topo.append(v)
    build_topo(self)
    # initialize the local gradient to 1
    self.grad = 1
    # accumulate gradients via back-propagation
    for v in reversed(topo):
      v._acc_grads()
