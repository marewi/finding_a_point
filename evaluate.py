import getopt
import pickle
import sys

from termcolor import colored


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
            if opt == '-s':
                print(f"param was {opt}")
                print(f"value was {args[0]}")
                filename = args[0]
                print(colored(f"filename set to: {filename}", 'green'))

    # TODO: access to qValues tbd
    # load calculated qValues
    with open(filename, 'rb') as f:
        q_table = pickle.load(f)

    print(q_table)

    # get arbitrary test pictures

    # run evaluating agent through test pictures


if __name__ == "__main__":
    main(sys.argv[1:])
