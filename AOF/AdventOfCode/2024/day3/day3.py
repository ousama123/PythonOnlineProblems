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
    data=str(data)
    dos = ""
    start = 0
    end = len(data)

    while start < len(data):
        end=data.find('don\'t()')
        while end != -1:
            dos += data[start:end]
            start = end + len("don't()")
            end = len(data[start:len(data)])
    
    print(dos)


def main():
    data=get_data()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()