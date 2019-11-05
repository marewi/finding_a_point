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

style.use("ggplot")

SIZE = 10 # size of square grid env

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
    
class Sqaure:
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
    
    # to subtract Sqaure from goal (pixel)
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

    for i in range(self.nrows):
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

# testing
agent = Sqaure()
goal = Goal(x=9,y=9)
print(agent)
print(agent-goal)
agent.action(0)
print(agent-goal)

#################################################################
# HERE STARTS MODEL DEVELOPMENT AND TRAINING

if start_q_table is None:
    q_table = {}
    for i in range(-SIZE+1, SIZE):
        for ii in range(-SIZE+1, SIZE):
            for iii in range(-SIZE+1, SIZE):
                for iiii in range(-SIZE+1, SIZE):
                    q_table[((i,ii),(iii,iiii))] = [np.random.uniform(-5,0) for i in range(4)]
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

print(q_table[((1,1),(1,1))])


# episode_rewards = []
# # for picture in range(all pictures):
# #     goal = Goal(x,y)
# #     for episode in range(EPISODES):
# #         agent = Sqaure()

# if episode % SHOW_EVERY == 0:
#     print(f"on #{episode}, epsilon is {epsilon}")
#     print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")

# episode_reward = 0
# for i in range(200): # TODO: why 200? -> maybe number of steps in episode
#     obs = {agent-goal}
#     print(obs)
#     if np.random.random() > epsilon:
#         action = np.argmax(q_table[obs]) # get action
#     else:
#         action = np.random.randint(0,4) # get action
#     agent.action(action) # take the action
#     # rewarding:
#     if agent.x == goal.x and agent.y == goal.y:
#         reward = GOAL_REWARD
#     else:
#         reward = -MOVE_PENALTY
#     new_obs = agent - goal # new observation
#     max_future_q = np.max(q_table[new_obs]) # max Q-value for this new obs
#     current_q = q_table[obs][action] # current Q for our chosen action
#     # calculations:
#     if reward == GOAL_REWARD:
#         new_q = GOAL_REWARD
#     else:
#         new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)



### testing
print("here starts testing area")
env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)  # starts an rbg of our size
env[goal.x][goal.y] = d[GOAL_N]  # sets the food location tile to green color
env[agent.x][agent.y] = d[AGENT_N]  # sets the player tile to blue
img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
img = img.resize((300, 300))  # resizing so we can see our agent in all its glory.
cv2.imshow("image", np.array(img))  # show it!
###