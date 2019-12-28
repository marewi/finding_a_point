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
    result = "SIZE: {SIZE}"
    
    return(result)