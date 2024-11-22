from dotenv import load_dotenv
import os
import math
 
load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def slope(grid, right, down):
    trees_count=0
    right_step=right
    rows = grid.splitlines()

    for r_idx in range(0, len(rows), down):
        row = rows[r_idx]
        value = row[right_step]

        if r_idx == 0:
            continue

        if value == '#':
            trees_count +=1

        right_step +=right

        if right_step >= len(row):
            right_step -= len(row)
    
    return trees_count
        

def main():
    moves = [
        (1, 1), 
        (3, 1), 
        (5, 1),  
        (7, 1), 
        (1, 2)   
    ]

    grid = get_data()
    #part1_trees_num=slope(grid, 3,1)
    #print(part1_trees_num)

    #part2
    slops=[slope(grid,right,down) for right, down in moves]
    print(math.prod(slops))

   
if __name__ == "__main__":
    main()