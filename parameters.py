# size of grid environment
SIZE = 100

# this is per training data (picture) -> 50000 per pic
EPISODES = 10000

MOVE_PENALTY = 1

GOAL_REWARD = 100

epsilon = 0.5

# every episode will be epsilon*EPISODE_DECAY
EPISODE_DECAY = 0.9999

# how often to play through env visually
SHOW_EVERY = 10

LEARNING_RATE = 0.1

DISCOUNT = 0.95