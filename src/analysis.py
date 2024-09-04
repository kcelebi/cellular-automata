import numpy as np
import automata as atm

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

# state is 3 dimensional matrix
def np_get_survival_stats(states):
	return np.apply_along_axis(lambda state: [get_total_alive(state), get_total_dead(state)], 1, states)

# each cell represents how many alive neighbors it has
'''
	This is super inefficient...
'''
def get_alive_matrix(state):
	x, y = state.shape
	alive_mat = np.zeros(state.shape)
	for i in range(x):
		for j in range(y):
			for neighbor_i, neighbor_j in atm.get_neighbors(i, j):
				if atm.in_range(neighbor_i, neighbor_j, state.shape):
					alive_mat[i, j] += state[neighbor_i, neighbor_j]

	return alive_mat
# ------------------------------

def get_random_state(shape):
	return np.random.randint(0, 2, size = shape)

# ------------------------------

def play(state, n, verbose = False):
	i = 0
	states = [state]
	while i < n and not is_terminal_state(state):
		if verbose:
			display_array(state)
			print(f'i={i}|-------')
		state = atm.update(state)
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
		finstr += "|\n"
	print(finstr)
