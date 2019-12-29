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
