import sys
sys.path.append('../')

import sim.automata as atm
from sim.rules import Rules

from machine_learning.q_learning_agents import QLearningAgent
from machine_learning.state import State

def run(init_state, rule =  Rules.CONWAY, **args):
	state = State(init_state, step_num = 0, rule = rule)

	agent = QLearningAgent(action_func = ..., reward_func = ..., **args)

	while ...:

		# observe the current state
		state = agent.observe_function(state)

		action = agent.get_action(state)

		agent.do_action(state, action)

		state = state.get_successor(action)



		print(f"Rewards: {agent.accum_train_rewards}")
