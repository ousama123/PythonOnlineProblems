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
        median_value=statistics.median(positions)
        pos_sum+= abs(median_value - pos)
    fuel_sums.append(pos_sum)

    return min(fuel_sums)

def part2(positions):
    #mean_value = statistics.mean(positions)
    lowest_mean, highest_mean = positions[0], positions[-1]
    all_fuel_costs = 0
    all_fule_costs_with_different_means = []
    for mean_val in range(lowest_mean, highest_mean+1):
        all_fuel_costs=0
        for pos in positions:
            dist=abs(mean_val - pos)
            fuel_cost = (dist * (dist + 1)) // 2
            all_fuel_costs += fuel_cost
        
        all_fule_costs_with_different_means.append((all_fuel_costs))

    print(min(all_fule_costs_with_different_means))
            
            
def main():
    data=get_data()
    positions=list(map(int,data.split(',')))
    positions = sorted(positions)
    fuel_sums=part1(positions)
    #print(int(fuel_sums))
    part2(positions)
   
if __name__ == "__main__":
    main()