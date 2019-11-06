# https://pythonprogramming.net/own-environment-q-learning-reinforcement-learning-python-tutorial/
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import xlrd
from prettytable import PrettyTable
from lib.generateplot import write_event

style.use("ggplot")

SIZE = 100 # size of square grid env

EPISODES = 100 # this is per training data (picture) # TODO: part of env?
MOVE_PENALTY = 1
GOAL_REWARD = 100
epsilon = 0.5 # TODO: part of env?
EPISODE_DECAY = 0.9999 # every episode will be epsilon*EPISODE_DECAY # TODO: part of env?
SHOW_EVERY = 10 # how often to play through env visually

start_q_table = None # here can be inserted a existing file

LEARNING_RATE = 0.1 # TODO: part of env?
DISCOUNT = 0.95 # TODO: part of env?

AGENT_N = 1 # key in dict for agent
GOAL_N = 2 # key in dict for goal (pixel)

# dict
d = { 1: (255, 175, 0), # blueish
      2: (0, 0, 0) } # black (pixel)

class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
    
class Square:
    def __init__(self):
        # self.x = np.random.randint(0, SIZE)
        # self.y = np.random.randint(0, SIZE)
        self.x = 0
        self.y = 0
        ### 
        # later: instead of starting in (0,0), 
        # start in state-action pair with greatest q-value
        ###

    # just a toString for debugging
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    # to subtract Square from goal (pixel)
    def __sub__(self, goal):
        return (self.x-goal.x, self.y-goal.y)

    def action(self, choice):
        '''
        4 different movement options:
            0. rechts: ++x
            1. links: --x
            2. runter: ++y
            3. hoch: --y
        '''
        if choice == 0:
            self.move(x=1)
        elif choice == 1:
            self.move(x=-1)
        elif choice == 2:
            self.move(y=1)
        elif choice == 3:
            self.move(y=-1)

    def move(self, x=False, y=False):
        self.x += x
        self.y += y

        # fix boundaries
        if self.x < 0:
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1

# TODO: put this in /lib
def sheetToString(self):
    '''
    converting sheet to string
    '''
    titles = []
    for iii in range(self.ncols):
        titles.append(str(self.cell_value(0,iii)))
    data = []
    t = PrettyTable(titles)

    for i in range(1,self.nrows):
        for ii in range(self.ncols):
            data.append(str(self.cell_value(i,ii)))
        t.add_row(data)
        data = []
    return(t)

# import coordinates from file
loc = ("./table.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheetToString(sheet))

# TODO: create goal with coordinates from file
first_x = sheet.cell_value(1,2)
first_y = sheet.cell_value(1,3)
print(f"first_x = {first_x} | first_y = {first_y}")

x_values = []
y_values = []
for i in range(1, sheet.nrows):
    x_values.append(sheet.cell_value(i,2))
for i in range(1, sheet.nrows):
    y_values.append(sheet.cell_value(i,3))

# PoC for incremental creating of an Goal
# for i in range(sheet.nrows-1):
#     print(f"x_position: {i} | x_value = {x_values[i]}")

# testing
# agent = Square()
# goal = Goal(x=9,y=9)
# print(agent)
# print(agent-goal)
# agent.action(0)
# print(agent-goal)

#################################################################
# HERE STARTS MODEL DEVELOPMENT AND TRAINING

if start_q_table is None:
    q_table = {}
    for i in range(-SIZE+1, SIZE):
        for ii in range(-SIZE+1, SIZE):
            q_table[(i,ii)] = [np.random.uniform(-5,0) for i in range(4)]
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

print(f"q_table: {q_table[(1,1)]}")

goals = []
episode_rewards = []
for pic_pos in range(sheet.nrows-1):
    goals.append(Goal(x_values[pic_pos],y_values[pic_pos]))
    print(f"goal created: nr = {pic_pos} | x = {goals[pic_pos].x} , y = {goals[pic_pos].y}")
    for episode in range(EPISODES):
        agent = Square()
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
    episode_reward = 0
    for i in range(2000): # TODO: why 2000? -> maybe number of steps in episode
        obs = agent-goals[pic_pos]
        print(f"i = {i} | obs: {obs}")
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
    # print(f"episode_reward: {episode_reward}")
    episode_rewards.append(episode_reward)
    epsilon *= EPISODE_DECAY

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

# TODO: dont save events in this dir because of git... this isnt so bad for logging for example
write_event(moving_avg, "moving_avg")