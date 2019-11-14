from parameters import SIZE
import numpy as np
from PIL import Image
from matplotlib import style
import time
from lib.toStringExt import sheetToString
from lib.generateplot import write_event

class Goal:
    def __init__(self, x, y, logo):
        self.x = x
        self.y = y
        self.logo = logo

    def __str__(self):
        return f"{self.x}, {self.y}, {self.logo}"
        
class Square:
    '''
    params:
        x: give an x-value as starting point
        y: give an y-value as starting point
    '''
    def __init__(self, x, y):
        # self.x = np.random.randint(0, SIZE)
        # self.y = np.random.randint(0, SIZE)
        self.x = x
        self.y = y

    # just a toString for debugging
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    # to subtract Square from goal (pixel)
    # def __sub__(self, goal):
    #     return (self.x-goal.x, self.y-goal.y)

    def action(self, choice):
        '''
        4 different movement options:
            0. rechts: ++x
            1. links: --x
            2. runter: ++y
            3. hoch: --y
        '''
        if choice == 0:
            self.move(x=1)
        elif choice == 1:
            self.move(x=-1)
        elif choice == 2:
            self.move(y=1)
        elif choice == 3:
            self.move(y=-1)

    def move(self, x=False, y=False):
        self.x += x
        self.y += y

        # fix boundaries
        if self.x < 0:
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1