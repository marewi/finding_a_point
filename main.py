from environment import Square, Goal
from model_table import Model_table
from parameters import GOAL_REWARD, MOVE_PENALTY, EPISODES, steps, epsilon, LEARNING_RATE, \
    DISCOUNT, EPISODE_DECAY, SHOW_EVERY
from q_learning import q_learning
from data_input import data_input
from lib.generateplot import write_event
from lib.toStringExt import sheetToString
import xlrd
import numpy as np
import operator
import time
import sys, getopt
from termcolor import colored

def main(argv):
    data_filter = ''
    try:
        opts, args = getopt.getopt(argv,"s")
        print(opts, args)
    except getopt.GetoptError:
        print(colored("option doesnt exist", 'red'))
        sys.exit(2)
    if args == []: 
        raise Exception(colored("no arguments", 'red'))
    if opts == []:
        print(f"no data_filter was set")
    else:
        for opt, _ in opts:
            print(f"opt: {opt}")
            if opt == '-s':
                print(f"param was {opt}")
                print(f"value was {args[0]}")
                data_filter = args[0]
                print(f"data_filter set to: {data_filter}")

    ######################################
    # create environment
    env_time = time.time()
    loc = "./data/table_300.xlsx"
    goals = data_input(loc, data_filter)

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

    # moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
    # print(f"moving_avg: {moving_avg}")
    # print(f"q_table: {q_table}")

    # show results
    # TODO: dont save events in this dir because of git... this isnt so bad for logging for example
    # write_event(moving_avg, "moving_avg")
    # write_event(epsilons, "epsilon")
    
if __name__ == "__main__":
    main(sys.argv[1:])