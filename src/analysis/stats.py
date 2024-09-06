import numpy as np

import sys
sys.path.append('../')

import sim.automata as atm
from sim.rules import Rules

# ------------------------------ STATS

def get_total_alive(state):
	state = atm.state_fix(state)
	return (state == 1).sum()

def get_total_dead(state):
	state = atm.state_fix(state)
	return (state == 0).sum()

def is_terminal_state(state):
	state = atm.state_fix(state)
	return get_total_alive(state) == 0

# ------------------------------ STAT MATRICES

def get_survival_stats(states):
	return np.array([get_total_alive(state) for state in states], dtype = int)

# each cell represents how many alive neighbors it has
'''
	O(8n^2)... whatever
'''
def get_alive_matrix(state):
	state = atm.state_fix(state)

	x, y = state.shape
	alive_mat = np.zeros(state.shape, dtype = int)
	for i in range(x):
		for j in range(y):
			# counts how many neighbors are alive (does not include self)
			for neighbor_i, neighbor_j in atm.get_neighbors(i, j, shape = state.shape):
				alive_mat[i, j] += state[neighbor_i, neighbor_j]


	return alive_mat