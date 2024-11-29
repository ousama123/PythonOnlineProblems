from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH_DEBUG) as f:
        return f.read()
    

def part1(grid):
    visible_trees = 0
    for row_idx in range(0,len(grid)):
        for col_idx in range(0,len(grid[0])):
            current = (grid[row_idx][col_idx])
            if (
                all(grid[row_idx][left_idx] < current for left_idx in range(col_idx ))
                or all(grid[row_idx][right_idx] < current for right_idx in range(col_idx + 1, len(grid[0])))
                or all(grid[upper_idx][col_idx] < current for upper_idx in range(row_idx ))
                or all(grid[lower_idx][col_idx] < current for lower_idx in range(row_idx + 1, len(grid)))
            ):
                visible_trees +=1
    print(visible_trees)
                
                            
def main():
    data=get_data()
    grid = [list(map(int, line)) for line in data.splitlines()]
    part1(grid)
    

if __name__ == "__main__":
    main()
            


