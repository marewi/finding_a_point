from parameters import SIZE
import numpy as np
from PIL import Image
from matplotlib import style
import time
from lib.toStringExt import sheetToString
from lib.generateplot import write_event

# class Environment:
#     def __init__(self):
#         # env_time = time.time()
#         self.Goal = self.Goal()
#         self.Square = self.Square()
        # # import coordinates (goals) from file
        # loc = ("./table.xlsx")
        # wb = xlrd.open_workbook(loc)
        # sheet = wb.sheet_by_index(0)
        # print(sheetToString(sheet))
        # x_values = []
        # y_values = []
        # for i in range(1, sheet.nrows):
        #     x_values.append(sheet.cell_value(i,2))
        # for i in range(1, sheet.nrows):
        #     y_values.append(sheet.cell_value(i,3))
        # self.goals = []
        # for pic_pos in range(sheet.nrows-1):
        #     self.goals.append(self.Goal(x_values[pic_pos],y_values[pic_pos]))
        #     print(f"goal created: nr = {pic_pos} | x = {self.goals[pic_pos].x} , y = {self.goals[pic_pos].y}")
        # print(f"--- time to create environment: {time.time()-env_time} ---")

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

# def createEnv():
    # # import coordinates (goals) from file
    # loc = ("./table.xlsx")
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)
    # print(sheetToString(sheet))

    # x_values = []
    # y_values = []
    # for i in range(1, sheet.nrows):
    #     x_values.append(sheet.cell_value(i,2))
    # for i in range(1, sheet.nrows):
    #     y_values.append(sheet.cell_value(i,3))

    # goals = []
    # for pic_pos in range(sheet.nrows-1):
    #     goals.append(Goal(x_values[pic_pos],y_values[pic_pos]))
    #     print(f"goal created: nr = {pic_pos} | x = {goals[pic_pos].x} , y = {goals[pic_pos].y}")

    # # PoC for creating a Goal incrementally
    # # for i in range(sheet.nrows-1):
    # #     print(f"x_position: {i} | x_value = {x_values[i]}")

    # # testing
    # # agent = Square()
    # # goal = Goal(x=9,y=9)
    # # print(agent)
    # # print(agent-goal)
    # # agent.action(0)
    # # print(agent-goal)

    # print(f"--- time to create environment: {time.time()-env_time} ---")
#################################################################
### HERE STARTS MODEL DEVELOPMENT
# model_time = time.time()

# if start_q_table is None:
#     q_table = {}
#     for i in range(-SIZE+1, SIZE):
#         for ii in range(-SIZE+1, SIZE):
#             q_table[(i,ii)] = [np.random.uniform(-5,0) for i in range(4)]
# else:
#     with open(start_q_table, "rb") as f:
#         q_table = pickle.load(f)
# print(f"q_table TEST: {q_table[(0,0)]}")

# print(f"--- time to create model: {time.time()-model_time} ---")
#################################################################
### HERE STARTS MODEL TRAINING
# training_time = time.time()

# episode_rewards = []
# epsilons = []
# for pic_pos in range(len(goals)):
#     # print(f"picture no: {pic_pos}")
#     for episode in range(EPISODES):
#         # print(f"\tepisode: {episode}")
#         agent = Square()
#         # if episode % SHOW_EVERY == 0:
#         #     print(f"\ton eps: {episode}, epsilon is {epsilon}")
#         #     print(f"\t{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
#         episode_reward = 0
#         for i in range(200): # TODO: why 200? -> maybe number of steps in episode
#             obs = agent-goals[pic_pos]
#             # print(f"i = {i} | obs: {obs}")
#             if np.random.random() > epsilon:
#                 action = np.argmax(q_table[obs]) # get action
#             else:
#                 action = np.random.randint(0,4) # get action
#             agent.action(action) # take the action
#             # rewarding:
#             if agent.x == goals[pic_pos].x and agent.y == goals[pic_pos].y:
#                 reward = GOAL_REWARD
#             else:
#                 reward = -MOVE_PENALTY
#             new_obs = agent - goals[pic_pos] # new observation
#             max_future_q = np.max(q_table[new_obs]) # max Q-value for this new obs
#             current_q = q_table[obs][action] # current Q for our chosen action
#             # calculations:
#             if reward == GOAL_REWARD:
#                 new_q = GOAL_REWARD
#             else:
#                 new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
#             q_table[obs][action] = new_q
#             episode_reward += reward
#             if reward == GOAL_REWARD:
#                 break
#         print(f"picture no: {pic_pos} | episode: {episode} | episode_reward: {episode_reward}")
#         episode_rewards.append(episode_reward)
#         epsilons.append(epsilon)
#         epsilon *= EPISODE_DECAY

# print(f"--- time to train model: {time.time()-model_time} ---")

# moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
# print(f"moving_avg: {moving_avg}")

# print(f"{q_table[0,0]}")

# # TODO: dont save events in this dir because of git... this isnt so bad for logging for example
# write_event(moving_avg, "moving_avg")
# write_event(epsilons, "epsilon")