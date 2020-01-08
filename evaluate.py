import getopt
import math
import operator
import pickle
import string
import sys

import numpy as np
from termcolor import colored

from dataInput import data_input
from environment import Agent
from parameters import *


def main(argv):
    filename = ''
    try:
        opts, args = getopt.getopt(argv,"f")
        print(opts, args)
    except getopt.GetoptError:
        print(colored("option doesnt exist", 'red'))
        sys.exit(2)
    if opts == [('-f', '')] and args == []: 
        raise Exception(colored("options for filename was set, but no arguments", 'red'))
    if opts == []:
        print(colored("no filename was set", 'red'))
    else:
        for opt, _ in opts:
            print(f"opt: {opt}")
            if opt == '-f':
                print(f"param was {opt}")
                print(f"value was {args[0]}")
                filename = args[0]
                print(colored(f"filename set to: {filename}", 'green'))

    # TODO: access to qValues tbd
    # load calculated qValues
    with open(filename, 'rb') as f:
        q_table = pickle.load(f)[0]

    print(q_table[127, 127])

    # get arbitrary test pictures
    data_filter = filename[12] # reading data_filter from filename 
    loc = "./data/table_3000_clustered.xlsx"
    goals = data_input(loc, data_filter)

    test_goals = []
    for _ in range(0, 10):
        test_goals.append(goals[np.random.randint(0, len(goals))])

    # run evaluating agent through test goals
    reward_sum = []
    for test_nr in range(len(test_goals)):
        # find state with max Q value
        x_of_state_with_max_q, y_of_state_with_max_q = max(q_table.items(), key=operator.itemgetter(1))[0]
        eva_agent = Agent(x_of_state_with_max_q, y_of_state_with_max_q)
        print(f"eva_agent created: {eva_agent}")
        for i in range(1000):
            state = (eva_agent.x, eva_agent.y)
            action = np.argmax(q_table[state]) # get action
            eva_agent.action(action)  # take the action
            print(f"eva_agent: {eva_agent}")
            if eva_agent.x == test_goals[test_nr].x and eva_agent.y == test_goals[test_nr].y:
                reward = GOAL_REWARD
            else:
                reward = -MOVE_PENALTY
            if eva_agent.x == test_goals[test_nr].x and eva_agent.y == test_goals[test_nr].y:
                reward_sum.append = reward
                print("now breaking...")
                break # reached goal
            print(reward)
    print(f"reward sum: {reward_sum}")

if __name__ == "__main__":
    main(sys.argv[1:])
