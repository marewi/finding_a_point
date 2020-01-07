import getopt
import pickle
import sys
import math

from termcolor import colored
from dataInput import data_input
from environment import Agent
import numpy as np
import string


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
    for i in range(len(test_goals)):
        eva_agent = Agent(test_goals[i].x, test_goals[i].y)
        for _ in range(1000)
        state = (eva_agent.x, eva_agent.y)
        action = np.argmax(q_table[state])  # get action
        eva_agent.action(action)  # take the action

if __name__ == "__main__":
    main(sys.argv[1:])
