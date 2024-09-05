import numpy as np
import automata as atm
from rules import Rules

def get_total_alive(state):
	if type(state) != np.array:
		state = np.array(state, dtype = int)
	return (state == 1).sum()

def get_total_dead(state):
	if type(state) != np.array:
		state = np.array(state, dtype = int)
	return (state == 0).sum()

def is_terminal_state(state):
	return get_total_alive(state) == 0

# ------------------------------

def get_survival_stats(states):
	return np.array([get_total_alive(state) for state in states], dtype = int)

# each cell represents how many alive neighbors it has
'''
	O(8n^2)... whatever
'''
def get_alive_matrix(state):
	x, y = state.shape
	alive_mat = np.zeros(state.shape)
	for i in range(x):
		for j in range(y):
			for neighbor_i, neighbor_j in atm.get_neighbors(i, j, shape = state.shape):
				alive_mat[i, j] += state[neighbor_i, neighbor_j]


	return alive_mat
# ------------------------------

def get_random_state(shape):
	return np.random.randint(0, 2, size = shape)

# ------------------------------

def play(state, steps, rule = Rules.CONWAY, verbose = False):
	if type(state) != np.array:
		state = np.array(state, dtype = int)

	i = 0
	states = [state]
	while i < steps and not is_terminal_state(state):
		if verbose:
			display_array(state)
			#print('-'*state.shape[1])
		state = atm.update(state, rule = rule)
		states += [state]
		i += 1
	
	return states

# ------------------------------ 

def display_array(state):
	x, y = state.shape

	finstr = ""
	for i in range(x):
		finstr += '|'
		for j in range(y):
			if state[i, j] == 1:
				finstr += "██"
			else:
				finstr += "  "
		finstr += ("|\n" + '--'*state.shape[1]*2)
	print(finstr)
