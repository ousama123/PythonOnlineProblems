from dotenv import load_dotenv
import os
import re

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH_DEBUG) as f:
        return f.read()

def part1(data):
    sum_nums= 0
    data=str(data)
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    matches = re.findall( pattern, data)
    for match in matches:
        left, right = match.split(",")
        num1= int(re.findall(r'[0-9]{1,3}', left)[0])
        num2= int(re.findall(r'[0-9]{1,3}', right)[0])
        sum_nums += num1 * num2
        
    print(sum_nums)

def part2(data):
    data = str(data)
    start_word = 'do()'
    end_word = "don't()"
    start = 0
    dos=""
    data =f"{start_word}{data}"

    while start < len(data):
        start = data.find(start_word, start)
        if start == -1: #if we dont find a start word
            break
        
        end = data.find(end_word, start)
        if end == -1: #if wee dont find an end word
            end=len(data)
            dos += data[start:end]
            break

        dos += data[start:end]
        start = end + len(end_word)
    
    part1(dos)

def main():
    data=get_data()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()