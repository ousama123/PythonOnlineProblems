from dotenv import load_dotenv
import os
import statistics
 
load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH_DEBUG) as f:
        return f.read()
    
def part1(positions):
    pos_sum=0
    fuel_sums=[]
    for pos in positions:
        pos_sum+= abs(statistics.median(positions) - pos)
    fuel_sums.append(pos_sum)

    return min(fuel_sums)

def part2(positions):
    step = 0 
    sum_pos=0
    sum_list = []
    for pos in positions:
        sum_pos=0
        for pos2 in positions:
            step=0
            if pos > pos2:
                for fuel in range(pos2, pos):        
                    step +=1
            if pos<pos2:
                for fuel in range(pos,pos2):
                    step +=1
            if pos == pos2:
                step +=0
            
            print(f"Move from {pos2} to {pos}: ", step, " fuel")
            sum_pos+=step
        sum_list.append(sum_pos)
        print(f"Sum for position {pos} is: " , sum_pos)
        print()
    print(min(sum_list))
            

def main():
    data=get_data()
    positions=list(map(int,data.split(',')))
    positions = sorted(positions)
    fuel_sums=part1(positions)
    print(int(fuel_sums))
    #part2(positions)
   
if __name__ == "__main__":
    main()