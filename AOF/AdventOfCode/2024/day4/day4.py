from dotenv import load_dotenv
import os
import re

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH_DEBUG) as f:
        return f.read()

def get_grid(data):
    grid=[]
    for line in data.splitlines():
        grid.append(line)
    return grid

def part1(data):
    word = 'XMAS'
    word_reverse= 'SAMX'
    cnt = 0
    for r in range(len(data)):    
        for c in range(len(data[0])):
            if data[r][c] == 'X':

                if c+4 <= len(data[0]):
                    right=data[r][c:c+4]
                if c-3 >= 0 :
                    left = data[r][c-3:c+1]
                if r-3 >= 0:
                    up = data[r-3:r+1][c]
                if r+4 <= len(data):
                    down = data[r:r+4][c]

                if (right)==word:
                    cnt +=1
                if (left)==word_reverse:
                    cnt +=1
                if (up)==word_reverse:
                    cnt +=1
                if (down)==word:
                    cnt +=1

    print(cnt)

def part2(data):
    pass

def main():
    data=get_data()
    data=get_grid(data)
    #print(data)
    part1(data)
    #part2(data)

if __name__ == "__main__":
    main()