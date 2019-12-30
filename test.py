# import math
# import operator
# import xlrd

# import numpy as np
# from prettytable import PrettyTable

# from lib.toStringExt import sheetToString
# from model_table import Model_table


# qtable = Model_table().q_table
# pt = PrettyTable()
# col = []
# x, y = max(qtable.items(), key=operator.itemgetter(1))[0]

# for i in range(0, int(math.sqrt(len(qtable)))):
#     for ii in range(0, int(math.sqrt(len(qtable)))):
#         pos_of_max_qvalue = np.argmax(qtable[i,ii])
#         if pos_of_max_qvalue == 0:
#             direction = "→"
#         elif pos_of_max_qvalue == 1:
#             direction = "←"
#         elif pos_of_max_qvalue == 2:
#             direction = "↓"
#         elif pos_of_max_qvalue == 3:
#             direction = "↑"
#         if i == x and ii == y:
#             direction += "⬤"
#         col.append(direction)
#     pt.add_column(f"x{i}", col)
#     col = []

# text_file = open("./logs/qtable_directions.txt", "w")
# text_file.write(str(pt))
# text_file.close()

# # ← → ↑ ↓ start:⬤  
# # ziel:◯