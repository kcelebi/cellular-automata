import numpy as np

'''
	Automata is state by state
	Note: might be better to do this in C for speedup

	idea -- create reinforcement learning model
	- we have state, action
	- model learns to add points to the CA state to achieve some outcome
'''



'''
	Brute force update -- O(n^2)
'''
def update(state):
	x, y = state.shape
	new_state = np.zeros(state.shape)

	for i in range(x):
		for j in range(y):
			neighbors = get_neighbors(i, j)
			alive = 0

			for [neighbor_i, neighbor_j] in neighbors:
				if in_range(neighbor_i, neighbor_j, state.shape):
					alive += state[neighbor_i, neighbor_j]

			# cell death condition
			if state[i, j] == 1 and (alive < 2 or alive > 3):
				new_state[i, j] = 0
			# cell rebirth condition
			elif state[i, j] == 0 and alive == 3:
				new_state[i, j] = 1
			# nothing, copy to new state
			else:
				new_state[i, j] = state[i,j]

	return new_state

def np_update(state):
	x, y = state.shape
	new_state = np.zeros(state.shape)



	# write a lambda to generate the update
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