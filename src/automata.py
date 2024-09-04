import numpy as np

'''
	Automata is state by state
	Note: might be better to do this in C for speedup

	idea -- create reinforcement learning model
	- we have state, action
	- model learns to add points to the CA state to achieve some outcome
'''

def play(state, n):
	for _ in range(n):
		display_array(state)
		state = update(state)

def display_array(mat):
	y = len(mat)
	x = len(mat[0])

	finstr = ""
	for y_ in range(y):
		for x_ in range(x):
			if mat[y_][x_] == 1:
				finstr += "██"
			else:
				finstr += "    "
		finstr += "\n"
	print(finstr)


'''
	Brute force update -- O(n^2)
'''
def update(state):
	x, y = len(state), len(state[0])
	new_state = [[0]*y]*x

	for i in range(x):
		for j in range(y):
			neighbors = get_neighbors(i, j)
			alive = 0

			for neighbor_i, neighbor_j in neighbors:
				if in_range(neighbor_i, neighbor_j, state):
					alive += state[neighbor_i][neighbor_j]

			# cell death condition
			if state[i][j] == 1 and (alive < 2 or alive > 3):
				new_state[i][j] = 0
			# cell rebirth condition
			elif state[i][j] == 0 and alive == 3:
				new_state[i][j] = 1
			# nothing, copy to new state
			else:
				new_state[i][j] = state[i][j]

	return new_state

def np_update(state):
	x, y = state.shape
	new_state = np.zeros(state.shape)

	# write a lambda to generate the update
	return 


def get_neighbors(i, j):
	# we can do this using matmult
	return np.reshape([[[i + u, j + v] for u in [-1, 1]] for v in [-1, 1]], -1)

def in_range(i, j, state):
	if i < len(state) and i > -1 and j > -1 and j < len(state[0]):
		return True
	return False