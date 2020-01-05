import getopt
import pickle
import sys

from termcolor import colored
import numpy as np


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
        q_table = pickle.load(f)

    # get arbitrary test pictures
    arbNumbers = []
    arbNumbers.append = np.random.randint(0, len(q_table)-1, 10)

    small_q_table = []
    for i in range(0, len(arbNumbers)):
        small_q_table.append = q_table[i]

    print(f"small_q_table: {small_q_table}")

    # run evaluating agent through test pictures


if __name__ == "__main__":
    main(sys.argv[1:])
