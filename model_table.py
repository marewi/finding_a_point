from parameters import SIZE
import numpy as np
import pickle
import time

class Model_table:
    def __init__(self):
        model_time = time.time()
        self.q_table = {}
        start_q_table = None # here can be inserted a existing file
        # print(str(range(-SIZE+1, SIZE)))
        if start_q_table is None:
            # self.q_table = {}
            # i,ii = {-127;128}
            for i in range(-SIZE+1, SIZE):
                for ii in range(-SIZE+1, SIZE):
                    self.q_table[(i,ii)] = [np.random.uniform(-5,0) for i in range(4)]
        # else:
        #     with open(start_q_table, "rb") as f:
        #         self.q_table = pickle.load(f)
        print(f"q_table TEST: {self.q_table[(0,0)]}")
        print(f"--- time to create q-table model: {time.time()-model_time} ---")