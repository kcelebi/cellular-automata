import sys
sys.path.append('../')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules


__all__ = ['ReinforcementAgent']

class Agent:

	def __init__(self, index = 0):
		self.index = index

	def get_action(self, state):
		raise NotImplementedError()


class ValueEstimationAgent(Agent):
	
	"""
		Abstract agent which assigns values to (state,action)
		Q-Values for an environment. As well as a value to a
		state and a policy given respectively by,

		V(s) = max_{a in actions} Q(s,a)
		policy(s) = arg_max_{a in actions} Q(s,a)

		Both ValueIterationAgent and QLearningAgent inherit
		from this agent. While a ValueIterationAgent has
		a model of the environment via a MarkovDecisionProcess
		(see mdp.py) that is used to estimate Q-Values before
		ever actually acting, the QLearningAgent estimates
		Q-Values while acting in the environment.
	"""

	def __init__(self, alpha = 1.0, epsilon = 0.05, gamma = 0.8, num_training = 10):
		'''
			alpha    - learning rate
			epsilon  - exploration rate
			gamma    - discount factor
			num_training - number of training episodes, i.e. no learning after these many episodes
		'''
		self.alpha = alpha
		self.epsilon = epsilon
		self.gamma = gamma
		self.num_training = num_training

	def get_Q_value(self, state, action):
		raise NotImplementedError()

	def get_value(self, state):
		raise NotImplementedError()

	def get_policy(self, state):
		raise NotImplementedError()

	def get_action(self, state):
		raise NotImplementedError()

class ReinforcementAgent(ValueEstimationAgent):

	def update(self, state, action, next_state, reward):
		raise NotImplementedError()


	'''
		Provided custom action_func -- to be overloaded into a new class

		Provides the possible legal actions for CA agent
	'''
	def get_legal_actions(self, state):
		return self.action_func(state)

	'''
		Called by observe_func after we have actually transitioned ot next state 
		-- then we have to record it
	'''
	def observe_transition(self, state, action, next_state, delta_reward):
		self.episode_rewards += delta_reward
		self.update(state, action, next_state, delta_reward)


	'''
		At each point in the game, we observe the state we have just arrived at
		and assess how that affects our score. 
	'''
	def observe_function(self, state):

		# ensure we don't call at first episode
		if self.last_state is not None:
			delta_reward = self.reward_func(state) - self.reward_func(self.last_state)
			
			self.observe_transition(
				state = self.last_state,
				action = self.last_action,
				next_state = state,
				delta_reward = delta_reward
			)

		return state

	def do_action(self, state, action):
		self.last_state = state
		self.last_action = action

	'''
		Called by env when new episode is starting
	'''
	def start_episode(self):
		self.last_state = None
		self.last_action = None
		self.episode_rewards = 0.0

	'''
		Called by env at the end of an episode
	'''
	def stop_episode(self):
		if self.is_in_training():
			self.accum_train_rewards += self.episode_rewards
		else:
			self.accum_test_rewards += self.episode_rewards

		self.episodes_so_far += 1

		# stop the learning for testing stage
		if self.is_in_testing:
			self.epsilon = 0.0 		# no exploration
			self.alpha = 0.0 		# no learning


	def is_in_training(self):
		return self.episodes_so_far < self.num_training

	def is_in_testing(self):
		return not self.is_in_training()
	

	'''
		action_func: Function which takes a state and returns the list of legal actions

		alpha    - learning rate
		epsilon  - exploration rate
		gamma    - discount factor
		numTraining - number of training episodes, i.e. no learning after these many episodes
	'''
	def __init__(self, action_func = None, reward_func = None, num_training = 100, epsilon = 0.5, alpha = 0.5, gamma = 1):

		self.action_func = action_func
		self.reward_func = reward_func
		self.episodes_so_far = 0
		self.accum_train_rewards = 0.0
		self.accum_test_rewards = 0.0
		self.num_training = int(num_training)
		self.epsilon = float(epsilon)
		self.alpha = float(alpha)
		self.discount = float(gamma)


	def final(self, state):
		delta_reward = get_score() - self.last_state.get_score()
		#... finsih implementing later

	





