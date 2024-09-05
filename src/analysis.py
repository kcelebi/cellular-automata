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

# ------------------------------ VERBOSE FUNCTIONS

'''
	Print the states out in ASCII form to command line
'''
def display_state(state):
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

'''
	Use matplotlib to plot a state, works for 1D as well
'''
def plot_state(state):
	fig, axs = plt.subplots()
	if state.shape[0] > 1:
		axs.imshow(~state[0], cmap = 'gray')
	else:
		axs.imshow(~state, cmap = 'gray')
	
	axs.set_xticks(np.arange(len(state))+0.5)
	axs.set_yticks(np.arange(len(state))+0.5)
	axs.set_xticklabels([])
	axs.set_yticklabels([])
	axs.grid()
	plt.show()

# ------------------------------

def play(state, steps, rule = Rules.CONWAY, verbose = False, verbose_func = display_state):
	if type(state) != np.array:
		state = np.array(state, dtype = int)

	i = 1
	states = np.zeros((steps, *state.shape), dtype = int)
	states[0, :, :] = state
	while i < steps and not is_terminal_state(state):
		if verbose:
			verbose_func(state)
		
		state = atm.update(state, rule = rule)
		states[i, :, :] = state
		i += 1
	
	return states
