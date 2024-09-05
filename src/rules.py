from enum import Enum
import automata as atm

# instead of just conway's, define a 
# lambda for arbitrary rule sets
# input is neighbors and current cell, 
# output is decision on new state at that cell

def _CONWAY(neighbors, cell, state):
	alive = 0
	for [neighbor_i, neighbor_j] in neighbors:
		if atm.in_range(neighbor_i, neighbor_j, state.shape):
			alive += state[neighbor_i, neighbor_j]

	# cell death condition
	if cell == 1 and (alive < 2 or alive > 3):
		return 0
	# cell rebirth condition
	elif cell == 0 and alive == 3:
		return 1
	# nothing, copy current state to new state
	else:
		return cell

'''
	Assumes 1D state (shape = (-1, 1))
'''
def _RULE30(neighbors, cell, state):
	assert state.shape[0] == 1, "Must provide 1D state for RULE30"

	if neighbors.shape[0] == 2:
		return int(bool(state[neighbors[0, 0], neighbors[0, 1]]) != bool(cell or state[neighbors[1, 0], neighbors[1, 1]]))

	elif neighbors.shape[0] == 1:
		return int(state[neighbors[0, 0], neighbors[0, 1]] or cell)

	else:
		# there is a shape issue
		# get back to this
		return -1

class Rules(Enum):
	CONWAY = _CONWAY
	RULE30 = _RULE30


