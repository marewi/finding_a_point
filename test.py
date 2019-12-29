import operator
import numpy as np

from prettytable import PrettyTable

from lib.toStringExt import sheetToString
from model_table import Model_table


qtable = Model_table().q_table

sheet = PrettyTable()

print(qtable)

# for i in range(0, len(qtable)-1):
#     for ii in range(0, len(qtable)-1):
#         a = np.argmax(qtable[i,ii])
#         print(a)


# print(sheetToString(sheet))
