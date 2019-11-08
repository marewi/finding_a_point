from environment import createEnv
from model_table import Model_table
from q_learning import moving_avg, epsilons
from lib.generateplot import write_event

# create environment
createEnv()

# build model
model = Model_table()

# train model


# show results
# TODO: dont save events in this dir because of git... this isnt so bad for logging for example
write_event(moving_avg, "moving_avg")
write_event(epsilons, "epsilon")