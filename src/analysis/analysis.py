import numpy as np

import sys
sys.path.append('../')

import sim.automata as atm
from sim.rules import Rules



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
		finstr += ("|\n")
	print(finstr + '--'*state.shape[1]*2)

'''
	Use matplotlib to plot a state, works for 1D as well
'''
def plot_state(state):
	state = atm.state_fix(state)

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

