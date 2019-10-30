# https://pythonprogramming.net/own-environment-q-learning-reinforcement-learning-python-tutorial/
import numpy as numpy
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time

style.use("ggplot")

SIZE = 100 # size of square grid env

EPISODES = 100
MOVE_PENALTY = 1
GOAL_REWARD = 100
epsilon = 0.5
EPISODE_DECAY = 0.9999 # every episode will be epsilon*EPISODE_DECAY
# SHOW_EVERY = 10 # how often to play through env visually

start_q_table = None # here can be inserted a existing file

LEARNING_RATE = 0.1
DISCOUNT = 0.95

AGENT_N = 1 # key in dict for agent
GOAL_N = 2 # key in dict for goal (pixel)

# dict
d = { 1: (255, 175, 0), # blueish
      2: (0, 0, 0) } # black (pixel)
    
class Sqaure:
    def __init__(self):