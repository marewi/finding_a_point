from environment import Goal
from lib.toStringExt import sheetToString
import xlrd
from termcolor import colored

def data_input(filename, data_filter):
    ''' data_input(filename, data_filter) -> goals

    import data from file
    '''
    loc = (filename)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheetToString(sheet))
    x_values = []
    y_values = []
    logo_values = []
    for row in range(1, sheet.nrows):
        if data_filter in  ['', sheet.cell_value(row,1)]:
            x_values.append(sheet.cell_value(row,2))
            y_values.append(sheet.cell_value(row,3))
            logo_values.append(sheet.cell_value(row,1))
    print("filter done! now creating goals")
    # create Goals with values
    goals = []
    for pic_pos in range(len(x_values)): # x_values for example
        goals.append(Goal(x_values[pic_pos],y_values[pic_pos], logo_values[pic_pos]))
        print(colored(f"goal created: {goals[pic_pos]}", 'white'))
    print(colored(f"{len(goals)} goals were created", 'green'))
    return goals