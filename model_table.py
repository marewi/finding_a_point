from parameters import SIZE
import numpy as np
import pickle

class Model_table:
    def __init__(self):
        self.q_table = {}
        start_q_table = None # here can be inserted a existing file
        # print(str(range(-SIZE+1, SIZE)))
        if start_q_table is None:
            # i,ii = {0;127}
            for i in range(0, SIZE):
                for ii in range(0, SIZE):
                    self.q_table[(i,ii)] = [np.random.uniform(-5,0) for i in range(4)]
        # else:
        #     with open(start_q_table, "rb") as f:
        #         self.q_table = pickle.load(f)
        print(f"q_table TEST: {self.q_table[(127,127)]}")