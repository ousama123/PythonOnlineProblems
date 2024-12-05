from dotenv import load_dotenv
import os
import re

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def get_grid(data):
    grid=[]
    for line in data.splitlines():
        grid.append((line))
    return (grid)

def part1(data):
    word = 'XMAS' 
    word_reverse= 'SAMX' 
    cnt = 0
    for r in range(len(data)):    
        for c in range(len(data[0])):
            if data[r][c] == 'X':
                right, left, up, down, up_left, up_right, down_left, down_right  = "", "", "", "", "", "", "", ""

                if c+4 <= len(data[0]):
                    right=data[r][c:c+4]
                if c-3 >= 0 :
                    left = data[r][c-3:c+1]
                if r-3 >= 0:
                    up = ''.join([data[el][c] for el in range(r-3,r+1)])
                if r+4 <= len(data):
                    down = ''.join([data[el][c] for el in range(r,r+4)])

                if c-3 >= 0 and r-3 >= 0:
                    up_left=''.join([data[r-i][c-i] for i in range(4)])
                if c+3 < len(data[0]) and r-3 >= 0:
                    up_right = ''.join([data[r-i][c+i] for i in range(4)])
                if c-3 >= 0 and r+3 < len(data):
                    down_left = ''.join([data[r+i][c-i] for i in range(4)])
                if r+3 < len(data) and c + 3 < len(data[0]):
                    down_right = ''.join([data[r+i][c+i] for i in range(4)])

                if right==word:
                    cnt +=1
                if left==word_reverse:
                    cnt +=1
                if up==word_reverse:
                    cnt +=1
                if down==word:
                    cnt +=1
 
                if up_left==word:
                    cnt +=1
                if up_right==word:
                    cnt +=1
                if down_left==word:
                    cnt +=1
                if down_right==word:
                    cnt +=1

    print(cnt)

def part2(data):
    word = 'MAS' 
    word_reverse= 'SAM' 
    cnt = 0
    for r in range(len(data)):    
        for c in range(len(data[0])):
            if data[r][c] == 'M':
                up_left, up_right, down_left, down_right  = "", "", "", ""

                if c-2 >= 0 and r-2 >= 0:
                    up_left=''.join([data[r-i][c-i] for i in range(3)])
                if c+2 < len(data[0]) and r-2 >= 0:
                    up_right = ''.join([data[r-i][c+i] for i in range(3)])
                if c-2 >= 0 and r+2 < len(data):
                    down_left = ''.join([data[r+i][c-i] for i in range(3)])
                if r+2 < len(data) and c + 2 < len(data[0]):
                    down_right = ''.join([data[r+i][c+i] for i in range(3)])
 
                if up_left==word:
                    cnt +=1
                if up_right==word:
                    cnt +=1
                if down_left==word:
                    cnt +=1
                if down_right==word:
                    cnt +=1

    print(cnt)

def main():
    data=get_data()
    data=get_grid(data)
    #print(data)
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()