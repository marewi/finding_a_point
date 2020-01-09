from parameter_optimization.environment import Agent
from parameter_optimization.testNN import testNN
from parameter_optimization.modelTable import Model_table

import numpy as np

epsilon = 0.5
q_table = Model_table()

for _ in range(10):
    for episode in range(10):
        agent = Agent(param1=0, param2=0)
        episode_reward = 0
        for step in range(10):
            state = (agent.param1, agent.param2)
            if np.random.random() > epsilon:
                action = np.argmax(...)
