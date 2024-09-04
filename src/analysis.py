import numpy as np
import automata as atm

def get_total_alive(state):
	return (state == 1).sum()

def get_total_dead(state):
	return (state == 0).sum()

def get_survival_stats(states):
	return np.array([[get_total_alive(state), get_total_dead(state)] for state in states])

# state is 3 dimensional matrix
def get_survival_stats(states):
	return np.apply_along_axis(lambda state: [get_total_alive(state), get_total_dead(state)], 1, states)
