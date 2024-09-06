import sys
sys.path.append('../')

from machine_learning.learning_agents import *
from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules


class QLearningAgent(ReinforcementAgent):

	def __init__(self, **args):
		ReinforcementAgent.__init__(self, **args)

		self.q_values = util.Counter()?