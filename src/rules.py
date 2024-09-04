import enum as Enum
import automata as atm

# instead of just conway's, define a 
# lambda for arbitrary rule sets
# input is neighbors and current cell, 
# output is decision on new state at that cell

class Rules:

	self.CONWAY = CONWAY
	self.RULE30 = lambda neighbors, cell, state: bool(neighbors[1]) != bool(cell or neighbors[-1])


def CONWAY(neighbors, cell, state):
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