# trainable.py
#
# Contains a Python class called "Trainable" that acts as a base class for all
# classes that contain parameters of Scalar objects subject to gradient updates

# Trainable class (acts as a base class for neural network components)
class Trainable:
  """
  Acts as a base class for neural network components with Scalar parameters
  """
  def parameters(self):
    return []

  def zero_grad(self):
    for p in self.parameters():
      p.grad = 0.0
