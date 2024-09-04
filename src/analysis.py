import numpy as np

def get_total_alive(state):
	if type(state) != np.array:
		state = np.array(state)
	return (state == 1).sum()

def get_total_dead(state):
	if type(state) != np.array:
		state = np.array(state)
	return (state == 0).sum()

def is_terminal_state(state):
	return get_total_alive(state) == 0

def get_survival_stats(states):
	return np.array([[get_total_alive(state), get_total_dead(state)] for state in states])

# state is 3 dimensional matrix
def np_get_survival_stats(states):
	return np.apply_along_axis(lambda state: [get_total_alive(state), get_total_dead(state)], 1, states)

def get_random_state(shape):
	return np.random.randint(0, 2, size = shape)