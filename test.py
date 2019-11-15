# from q_learning import q_learning
# from parameters import steps, epsilon, GOAL_REWARD, MOVE_PENALTY, EPISODES, LEARNING_RATE, DISCOUNT, EPISODE_DECAY, SHOW_EVERY
# from main import goals
# from main import model

# r, t = q_learning(EPISODES, goals, steps, epsilon, model, GOAL_REWARD, MOVE_PENALTY, LEARNING_RATE, DISCOUNT, EPISODE_DECAY)

# print(f"TEST::::::::::: {r}")

# import sys, getopt

# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv,"s")
#         print(opts, args)
#     except getopt.GetoptError:
#         print("sth went wrong")
#         sys.exit(2)
#     for opt, _ in opts:
#         if opt == '-s':
#             print(f"param was {opt}")
#     for arg in args:
#         if arg == 'hook':
#             print(f"value was {arg}")



# if __name__ == "__main__":
#    main(sys.argv[1:])