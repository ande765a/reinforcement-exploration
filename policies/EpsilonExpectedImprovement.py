import numpy as np
from policies import Policy

class EpsilonExpectedImprovement(Policy):
  def __init__(self, epsilon):
    super().__init__()
    self.epsilon = epsilon

  def pi(self, Q, s):
    """
    Expect Q to be defined as:
    def Q(s):
      return {
        0: (mean, std),
        1: (mean, std),
        4: (mean, std)
      }
    """
    actions = Q(s)
    action_keys = list(actions.keys())
    if np.random.rand() < self.epsilon:
      return np.random.choice(action_keys)
    else:
      # Return greedy action
      return action_keys[np.argmax([mean for mean, std in actions.values()])]

  def __str__(self):
    return f"epsilon-greedy-{self.epsilon}"