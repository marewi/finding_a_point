from parameters import SIZE
import numpy as np
import pickle
import time

class Model_table:
    def __init__(self):
        model_time = time.time()

        start_q_table = None # here can be inserted a existing file

        if start_q_table is None:
            q_table = {}
            for i in range(-SIZE+1, SIZE):
                for ii in range(-SIZE+1, SIZE):
                    q_table[(i,ii)] = [np.random.uniform(-5,0) for i in range(4)]
        else:
            with open(start_q_table, "rb") as f:
                q_table = pickle.load(f)
        print(f"q_table TEST: {q_table[(0,0)]}")

        print(f"--- time to create q-table model: {time.time()-model_time} ---")