from dotenv import load_dotenv
import os

from operator import add, mul
from itertools import product

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def part2(data):
    ops = [add, mul, "||"]
    all_resutls = []
    for line in data.splitlines():
        result=0
        test_val, nums = line.strip().split(":")
        test_val = int(test_val.strip())
        nums = list(map(int,nums.strip().split())) 
        combinations = product(ops, repeat=len(nums)-1)

        for comb in combinations:
            result = nums[0] 
            for i, op in enumerate(comb): 
                if op == "||":
                    result = int(f"{result}{nums[i + 1]}")
                else:
                    result = op(result, nums[i + 1])

            if result == test_val:
                all_resutls.append(result)
                break

    print(sum(all_resutls))

def part1(data):
    ops = [add, mul]
    all_resutls = []
    for line in data.splitlines():
        result=0
        test_val, nums = line.strip().split(":")
        test_val = int(test_val.strip())
        nums = list(map(int,nums.strip().split())) 
        combinations = product(ops, repeat=len(nums)-1)

        for comb in combinations:
            result = nums[0] 
            for i, op in enumerate(comb): 
                result = op(result, nums[i + 1])

            if result == test_val:
                all_resutls.append(result)
                break

    print(sum(all_resutls))

def main():
    data=get_data()
    #part1(data)
    part2(data)

        

if __name__ == "__main__":
    main()