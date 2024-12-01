from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def calc_distance(num1,num2):
    return abs(num1 - num2)

def part1(data):
    distances = 0
    left_ids=[]
    right_ids=[]
    for line in data.splitlines():
        left_id, right_id= line.split()
        left_ids.append(int(left_id))
        right_ids.append(int(right_id))
    
    left_ids.sort()
    right_ids.sort()
    distances =[calc_distance(left_ids[idx], right_ids[idx]) for idx in range(len(left_ids))]
    
    print(sum(distances))

def part2(data):
    similarity = 0
    similarity_score=0
    left_ids=[]
    right_ids=[]
    for line in data.splitlines():
        left_id, right_id= line.split()
        left_ids.append(int(left_id))
        right_ids.append(int(right_id))
    
    for num in left_ids:
        similarity = 0
        for num2 in right_ids:
            if num == num2:
                similarity +=1

        similarity_score +=num * similarity

    print(similarity_score)

def main():
    data=get_data()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()