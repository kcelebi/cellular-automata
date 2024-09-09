import numpy as np
from tqdm import tqdm, trange

import sys
sys.path.append('../')

import sim.automata as atm
from sim.rules import Rules

from machine_learning.q_learning_agents import QLearningAgent
from machine_learning.state import State

def run(init_state, agent episode_length = 10):
	#agent = QLearningAgent(action_func = action_func, reward_func = reward_func)
	
	state = init_state.copy()
	while agent.episodes_so_far < agent.num_training + 50:
		
		agent.start_episode()
		for i in trange(episode_length):
			_ = agent.observe_function(state)
			
			action = agent.get_action(state)
			agent.do_action(state, action)
			
			state = state.get_successor(action)
		
		agent.stop_episode()
		print(f"Train Rewards: {agent.accum_train_rewards}")
		print(f"Test Rewards: {agent.accum_test_rewards}\n")
	
	#return agent
