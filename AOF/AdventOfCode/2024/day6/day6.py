from dotenv import load_dotenv
import os
import re

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()
    
def turn_90_deg(current_state):
    if current_state == '<':
        return '^'

    if current_state == '^':
        return '>'

    if current_state == '>':
        return 'v'

    if current_state == 'v':
        return '<'

def move_forward(grid, i, j):
    current_state = grid[i][j]
    steps = 0

    while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        if current_state == '<':
            while j-1>0 and grid[i][j-1] !='#' :
                current_state = grid[i][j-1]
                steps +=1
                j = j-1
            #grid[i][j] = turn_90_deg('<')
            current_state = turn_90_deg('<')

        elif current_state == '^':
            while i-1>0 and grid[i-1][j] !='#' :
                current_state = grid[i-1][j]
                steps +=1
                i = i-1
            #grid[i][j] = turn_90_deg('^')
            current_state = turn_90_deg('^')

        elif current_state == '>': 
            while j+1<len(grid[0]) and grid[i][j+1] !='#' :
                current_state = grid[i][j+1]
                steps +=1
                j = j+1
            #grid[i][j] = turn_90_deg('>')
            current_state = turn_90_deg('>')

        elif current_state == 'v': 
            while i+1<len(grid) and grid[i+1][j] !='#' :
                current_state = grid[i+1][j]
                steps +=1
                i = i+1
            #grid[i][j] = turn_90_deg('v')
            current_state = turn_90_deg('v')
    
    print(steps)
    

def main():
    data=get_data()
    grid = []

    for line in data.splitlines():
        grid.append(list(line))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ('<', '^', '>', 'v'):
                move_forward(grid, i, j) 
                return
        

if __name__ == "__main__":
    main()