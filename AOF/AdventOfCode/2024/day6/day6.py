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
    steps = 1
    while j < len(grid[0]) and i < len(grid):
        if current_state == '<':
            while grid[i][j-1] !='#' and j>0:
                current_state = grid[i][j-1]
                steps +=1
                j = j-1
            grid[i][j] = turn_90_deg('<')
            current_state = grid[i][j]

        elif current_state == '^':
            while grid[i-1][j] !='#' and i>0:
                current_state = grid[i-1][j]
                steps +=1
                i = i-1
            grid[i][j] = turn_90_deg('^')
            current_state = grid[i][j]

        elif current_state == '>': 
            while grid[i][j+1] !='#' and j<len(grid[0]):
                current_state = grid[i][j+1]
                steps +=1
                j = j+1
            grid[i][j] = turn_90_deg('>')
            current_state = grid[i][j]

        elif current_state == 'v': 
            while grid[i+1][j] !='#' and i<len(grid):
                current_state = grid[i+1][j]
                steps +=1
                i = i+1
            grid[i][j] = turn_90_deg('v')
            current_state = grid[i][j]
    
    print(steps)
    

def main():
    data=get_data()
    grid = []
    steps=0
    for line in data.splitlines():
        line = list(line)
        grid.append(line)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current_state = grid[i][j]
            if current_state in ('<' , '^' , '>' , 'v'):
                move_forward(grid, i, j)
                return
        

if __name__ == "__main__":
    main()