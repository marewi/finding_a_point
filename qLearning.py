import operator
import time

import numpy as np
from termcolor import colored

from environment import Agent
from parameters import *


def q_learning(goals, model):
    ''' q_learning(goals, model) -> episode_rewards, q_table, epsilons

    parameters:
        goals: use this goals data...
        model: ...to train this model
    returns:
        episode_rewards: 
        q_table: trained model
        epsilons: decaying of epsilon
    '''
    global epsilon
    q_table = model.q_table
    x_of_state_with_max_q_old = 0
    y_of_state_with_max_q_old = 0
    episode_rewards = []
    epsilons = []
    for pic_pos in range(len(goals)):
        # reset epsilon for each new picture
        eps = epsilon
        print(colored(f"epsilon reset to {eps}", 'yellow'))
        for episode in range(EPISODES):
            # find state with max Q value
            x_of_state_with_max_q, y_of_state_with_max_q = max(
                q_table.items(), key=operator.itemgetter(1))[0]
            # let agent start in this state
            agent = Agent(x_of_state_with_max_q, y_of_state_with_max_q)
            # print new agent start if its coordinates have changed
            if x_of_state_with_max_q_old != x_of_state_with_max_q or y_of_state_with_max_q_old != y_of_state_with_max_q:
                print(colored(f"agent start has changed: {x_of_state_with_max_q_old, y_of_state_with_max_q_old} " +
                              f"--> {x_of_state_with_max_q, y_of_state_with_max_q}", 'yellow'))
            episode_reward = 0
            for _ in range(steps):
                state = (agent.x, agent.y)
                # if state[0] > SIZE-1 or state[0] < 0 or state[1] > SIZE-1 or state[1] < 0:
                #     print(f"i = {i} | state: {state}")
                if np.random.random() > eps:
                    action = np.argmax(q_table[state])  # get action
                else:
                    action = np.random.randint(0, 4)  # get action
                agent.action(action)  # take the action
                # rewarding:
                if agent.x == goals[pic_pos].x and agent.y == goals[pic_pos].y:
                    reward = GOAL_REWARD
                else:
                    reward = -MOVE_PENALTY
                new_state = (agent.x, agent.y)
                # max Q-value for this new state
                max_future_q = np.max(q_table[new_state])
                # current Q for our chosen action
                current_q = q_table[state][action]
                # Q value calculations:
                if reward == GOAL_REWARD:
                    new_q = GOAL_REWARD
                else:
                    new_q = (1 - LEARNING_RATE) * current_q + \
                        LEARNING_RATE * (reward + DISCOUNT * max_future_q)
                q_table[state][action] = new_q
                episode_reward += reward
                if reward == GOAL_REWARD:
                    break
            print(f"picture no: {pic_pos} | goal: {goals[pic_pos]} | episode: {episode} | " +
                  f"episode_reward: {episode_reward}")
            x_of_state_with_max_q_old = x_of_state_with_max_q
            y_of_state_with_max_q_old = y_of_state_with_max_q
            episode_rewards.append(episode_reward)
            epsilons.append(eps)
            eps *= EPISODE_DECAY
    return(episode_rewards, q_table, epsilons)
