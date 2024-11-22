from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def count_trees(grid):
    trs_count=0
    col_idx = 3
    for r_idx, row in enumerate(grid.splitlines()):
        if(r_idx == 0):
            continue
        
        value = row[col_idx]
        if value == '#':
            trs_count +=1
        
        col_idx +=3

        if col_idx >= len(row):
            col_idx -= len(row)
            
    return trs_count

def main():
    data = get_data()
    #print(data)
    trs_count=count_trees(data)
    print(trs_count)

   
if __name__ == "__main__":
    main()