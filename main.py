from environment import Square, Goal
from model_table import Model_table
from parameters import GOAL_REWARD, MOVE_PENALTY, EPISODES, steps, epsilon, LEARNING_RATE, DISCOUNT, EPISODE_DECAY, SHOW_EVERY
from lib.generateplot import write_event
from lib.toStringExt import sheetToString
import xlrd
import numpy as np
import time

######################################
# create environment
env_time = time.time()

# import coordinates (goals) from file
loc = ("./data/table_300.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheetToString(sheet))
x_values = []
y_values = []
for i in range(1, sheet.nrows):
    x_values.append(sheet.cell_value(i,2))
for i in range(1, sheet.nrows):
    y_values.append(sheet.cell_value(i,3))
goals = []
for pic_pos in range(sheet.nrows-1):
    goals.append(Goal(x_values[pic_pos],y_values[pic_pos]))
    print(f"goal created: nr = {pic_pos} | x = {goals[pic_pos].x} , y = {goals[pic_pos].y}")
print(f"--- time to create environment: {time.time()-env_time} ---")

######################################
# build model
model = Model_table()

######################################
# train model

# TODO: use q_learning() --> see test.py

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
        for i in range(steps):
            obs = agent-goals[pic_pos]
            # print(f"i = {i} | obs: {obs}")
            if np.random.random() > epsilon:
                action = np.argmax(model.q_table[obs]) # get action
            else:
                action = np.random.randint(0,4) # get action
            agent.action(action) # take the action
            # rewarding:
            if agent.x == goals[pic_pos].x and agent.y == goals[pic_pos].y:
                reward = GOAL_REWARD
            else:
                reward = -MOVE_PENALTY
            new_obs = agent - goals[pic_pos] # new observation
            max_future_q = np.max(model.q_table[new_obs]) # max Q-value for this new obs
            current_q = model.q_table[obs][action] # current Q for our chosen action
            # calculations:
            if reward == GOAL_REWARD:
                new_q = GOAL_REWARD
            else:
                new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            model.q_table[obs][action] = new_q
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

print(f"q_table: {model.q_table}")

# show results
# TODO: dont save events in this dir because of git... this isnt so bad for logging for example
write_event(moving_avg, "moving_avg")
write_event(epsilons, "epsilon")