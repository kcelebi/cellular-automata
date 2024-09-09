import numpy as np

import sys
sys.path.append('../')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules

class State:

	def __init__(self, state, step_num, rule):
		self.values = state
		self.step_num = step_num
		self.rule = rule

	# fix this dogshit hash function
	def __hash__(self):
		return hash(self.values.tostring())

	def __repr__(self):
		return self.values.__repr__()

	'''
		Generate successor states based on given action
	'''
	def get_successors(self, action):
		new_state = self.values.copy()
		new_state[action // self.values.shape[1], action % self.values.shape[1]] = 1
		new_state = atm.update(new_state, rule = self.rule)

		return State(new_state, step_num = self.step_num + 1, rule = self.rule)
