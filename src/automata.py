import numpy as np

'''
	Automata is state by state
	Note: might be better to do this in C for speedup

	idea -- create reinforcement learning model
	- we have state, action
	- model learns to add points to the CA state to achieve some outcome
	- consider: ask agent to create a certain state, or some qualification using k moves
			- how does it do it

	- we need pattern detection
	- we need cycle detection
		- can we transform each image to a graph...
		- each state to a graph? 

	- some web server where you can pkay / analyze differnet automata setup
		- have the interactive code etc
		- need to port it all to JS
'''



'''
	Brute force update -- O(n^2)

	NOTE: this is *not* updating in-place
'''
def update(state, rule):
	if type(state) != np.array:
		state = np.array(state, dtype = int)

	x, y = state.shape
	new_state = np.zeros(state.shape, dtype = int)

	for i in range(x):
		for j in range(y):
			neighbors = get_neighbors(i, j)
			new_state[i, j] = rule(neighbors, state[i, j], state)

	return new_state

def np_update(state):
	x, y = state.shape
	new_state = np.zeros(state.shape)

	# write a lambda to generate the update more efficiently
	return 


def get_neighbors(i, j):
	# we can do this using matmult
	neighbors = np.reshape([[[i + u, j + v] for u in [-1, 0, 1]] for v in [-1, 0, 1]], (-1, 2))
	return neighbors[~np.all(neighbors == [i, j], axis = 1)]

'''
	Check the provided coord is in range of the matrix
'''
def in_range(i, j, shape):
	if i < shape[0] and i > -1 and j > -1 and j < shape[1]:
		return True
	return False