from environment import Square, Goal
from model_table import Model_table
from parameters import GOAL_REWARD, MOVE_PENALTY, EPISODES, steps, epsilon, LEARNING_RATE, \
    DISCOUNT, EPISODE_DECAY, SHOW_EVERY
from q_learning import q_learning
from lib.generateplot import write_event
from lib.toStringExt import sheetToString
import xlrd
import numpy as np
import operator
import time
from termcolor import colored

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
logo_values = []
for i in range(1, sheet.nrows):
    x_values.append(sheet.cell_value(i,2))
    y_values.append(sheet.cell_value(i,3))
    logo_values.append(sheet.cell_value(i,1))
goals = []
for pic_pos in range(sheet.nrows-1):
    goals.append(Goal(x_values[pic_pos],y_values[pic_pos], logo_values[pic_pos]))
    print(colored(f"goal created: {goals[pic_pos]}", 'green'))
print(colored(f"--- time to create environment: {time.time()-env_time} ---", 'blue'))

######################################
# build model
model_time = time.time()
model = Model_table()
print(colored(f"--- time to create q-table model: {time.time()-model_time} ---", 'blue'))

######################################
# train model
learning_time = time.time()
episode_rewards, q_table, epsilons = q_learning(goals, model)
print(colored(f"--- time to train model: {time.time()-learning_time} ---", 'blue'))

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
# print(f"moving_avg: {moving_avg}")
# print(f"q_table: {q_table}")

# show results
# TODO: dont save events in this dir because of git... this isnt so bad for logging for example
write_event(moving_avg, "moving_avg")
write_event(epsilons, "epsilon")