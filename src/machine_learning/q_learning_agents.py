import random

import sys
sys.path.append('../')

from machine_learning.learning_agents import *
import machine_learning.util as util
from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules


class QLearningAgent(ReinforcementAgent):

	def __init__(self, **args):
		ReinforcementAgent.__init__(self, **args)

		# how are we going to implement this counter obj
		self.q_values = util.Counter()


	def get_Q_value(self, state, action):
		'''
			Returns Q(state,action)
			Should return 0.0 if we have never seen a state
			or the Q node value otherwise
		'''
		return self.q_values[(state, action)]

	def compute_value_from_Q_values(self, state):
		'''
			Returns max_action Q(state,action)
			where the max is over legal actions.  Note that if
			there are no legal actions, which is the case at the
			terminal state, you should return a value of 0.0.
		'''

		legal_actions = self.get_legal_actions(state)

		#Terminal
		if len(legal_actions) == 0:
			return 0.0

		return max([self.get_Q_value(state, a) for a in legal_actions])


	def compute_action_from_Q_values(self, state):
		"""
			Compute the best action to take in a state.  Note that if there
			are no legal actions, which is the case at the terminal state,
			you should return None.
		"""
		legal_actions = self.get_legal_actions(state)

		# Terminal
		if len(legal_actions) == 0:
			return None

		best = sorted([(a, self.get_Q_value(state, a)) for a in legal_actions], key = lambda x: x[1], reverse = True)
		return random.choice([b[0] for b in best if b[1] == best[0][1]])
	
	def get_action(self, state):
		legal_actions = self.get_legal_actions(state)

		# Terminal state
		if len(legal_actions) == 0:
			return None

		if random.random() < self.epsilon:
			return random.choice(legal_actions)
		return self.compute_action_from_Q_values(state)


	# update our q values here
	def update(self, state, action, next_state, reward):
		# from value estmation parent.parent
		NSQ = self.get_value(next_state)


		self.q_values[(state, action)] = self.get_Q_value(state, action) + self.alpha * (reward + self.discount*NSQ - self.get_Q_value(state, action))


	def get_policy(self, state):
		return self.compute_action_from_Q_values(state)

	def get_value(self, state):
		return self.compute_value_from_Q_values(state)


