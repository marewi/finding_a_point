import math
import operator

import numpy as np
from prettytable import PrettyTable

from parameters import *


def sheetToString(self):
    '''
    converting sheet to string
    '''
    titles = []
    for iii in range(self.ncols):
        titles.append(str(self.cell_value(0,iii)))
    data = []
    table = PrettyTable(titles)

    for i in range(1,self.nrows):
        for ii in range(self.ncols):
            data.append(int(self.cell_value(i,ii)))
        table.add_row(data)
        data = []
        
    return(table)

def paremetersToString():
    '''
    converting all learning parameters to string
    '''
    result = ('PAREMETER SETTINGS\n'
             f'SIZE: {SIZE}x{SIZE}\n'
             f'EPISODES: {EPISODES}\n'
             f'steps: {steps}\n'
             f'MOVE_PENALTY: {MOVE_PENALTY}\n'
             f'GOAL_REWARD: {GOAL_REWARD}\n'
             f'epsilon: {epsilon}\n'
             f'EPISODE_DECAY: {EPISODE_DECAY}\n'
             f'LEARNING_RATE: {LEARNING_RATE}\n'
             f'DISCOUNT: {DISCOUNT}')
    
    return(result)

def qtableToString(self, directions=False):
    '''
    directions=False: converting qtable values to string
    directions=True: converting qtable values to direction strings
    '''
    pt = PrettyTable()
    col = []
    x, y = max(self.items(), key=operator.itemgetter(1))[0]

    for i in range(0, int(math.sqrt(len(self)))):
        for ii in range(0, int(math.sqrt(len(self)))):
            if directions == True:
                pos_of_max_qvalue = np.argmax(self[i,ii])
                if pos_of_max_qvalue == 0:
                    direction = "→"
                elif pos_of_max_qvalue == 1:
                    direction = "←"
                elif pos_of_max_qvalue == 2:
                    direction = "↓"
                elif pos_of_max_qvalue == 3:
                    direction = "↑"
                if i == x and ii == y:
                    direction += "⬤"
                col.append(direction)
            elif directions == False:
                qValues = f""
                for iii in range(0, len(self[i,ii])): 
                    qValues += f"{self[i,ii][iii]}" + "\n"
                col.append(qValues)
        pt.add_column(f"x={i}", col)
        col = []

    # ← → ↑ ↓ start:⬤  
    # ziel:◯

    return(pt)
