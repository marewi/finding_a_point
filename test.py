from q_learning import q_learning
from parameters import steps, epsilon, GOAL_REWARD, MOVE_PENALTY, EPISODES, LEARNING_RATE, DISCOUNT, EPISODE_DECAY, SHOW_EVERY
from main import goals
from main import model

r, t = q_learning(EPISODES, goals, steps, epsilon, model, GOAL_REWARD, MOVE_PENALTY, LEARNING_RATE, DISCOUNT, EPISODE_DECAY)

print(f"TEST::::::::::: {r}")

