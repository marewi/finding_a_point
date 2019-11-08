from parameters import GOAL_REWARD, MOVE_PENALTY, EPISODES, LEARNING_RATE, DISCOUNT, EPISODE_DECAY, SHOW_EVERY
from environment import Square, goals
from model_table import q_table
import numpy as np
import time

learning_time = time.time()

episode_rewards = []
epsilons = []
for pic_pos in range(len(goals)):
    # print(f"picture no: {pic_pos}")
    for episode in range(EPISODES):
        # print(f"\tepisode: {episode}")
        agent = Square()
        # if episode % SHOW_EVERY == 0:
        #     print(f"\ton eps: {episode}, epsilon is {epsilon}")
        #     print(f"\t{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        episode_reward = 0
        for i in range(200): # TODO: why 200? & putting in parameters
            obs = agent-goals[pic_pos]
            # print(f"i = {i} | obs: {obs}")
            if np.random.random() > epsilon:
                action = np.argmax(q_table[obs]) # get action
            else:
                action = np.random.randint(0,4) # get action
            agent.action(action) # take the action
            # rewarding:
            if agent.x == goals[pic_pos].x and agent.y == goals[pic_pos].y:
                reward = GOAL_REWARD
            else:
                reward = -MOVE_PENALTY
            new_obs = agent - goals[pic_pos] # new observation
            max_future_q = np.max(q_table[new_obs]) # max Q-value for this new obs
            current_q = q_table[obs][action] # current Q for our chosen action
            # calculations:
            if reward == GOAL_REWARD:
                new_q = GOAL_REWARD
            else:
                new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[obs][action] = new_q
            episode_reward += reward
            if reward == GOAL_REWARD:
                break
        print(f"picture no: {pic_pos} | episode: {episode} | episode_reward: {episode_reward}")
        episode_rewards.append(episode_reward)
        epsilons.append(epsilon)
        epsilon *= EPISODE_DECAY

print(f"--- time to train model: {time.time()-learning_time} ---")

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
print(f"moving_avg: {moving_avg}")

print(f"{q_table[0,0]}")