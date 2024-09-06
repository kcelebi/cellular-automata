import sys
sys.path.append('../')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules


__all__ = ['ReinforcementAgent']

class Agent:

	def __init__(self, index = 0):
		self.index = index

	def get_action(self, state):
		raise NotImplementedError()


class ValueEstimationAgent(Agent):
	
	"""
      Abstract agent which assigns values to (state,action)
      Q-Values for an environment. As well as a value to a
      state and a policy given respectively by,

      V(s) = max_{a in actions} Q(s,a)
      policy(s) = arg_max_{a in actions} Q(s,a)

      Both ValueIterationAgent and QLearningAgent inherit
      from this agent. While a ValueIterationAgent has
      a model of the environment via a MarkovDecisionProcess
      (see mdp.py) that is used to estimate Q-Values before
      ever actually acting, the QLearningAgent estimates
      Q-Values while acting in the environment.
    """

	def __init__(self, alpha, epsilon, gamma, num_training):
		'''
	        alpha    - learning rate
	        epsilon  - exploration rate
	        gamma    - discount factor
	        num_training - number of training episodes, i.e. no learning after these many episodes
        '''
		self.alpha = alpha
		self.epsilon = epsilon
		self.gamma = gamma
		self.num_training = num_training

	def get_Q_value(self, state, action):
		...

	def get_value(self, state):
		...

	def get_policy(self, state):
		...

	def get_action(self, state):
		...

class ReinforcementAgent(ValueEstimationAgent):

	def update(self, state, action, next_state, reward):
		...

	def get_legal_actions(self, state):
		...

	def observe_transition(self, state, action, next_state, delta_reward):
		...



