from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def ckeck_increasing(report):
    for lvl in range(len(report)-1):
        if report[lvl+1] - report[lvl] not in [1,2,3]:
            return False
    return True
        
def ckeck_decreasing(report):
    for lvl in range(len(report)-1):
        if report[lvl] - report[lvl+1] not in [1,2,3]:
            return False
    return True


def part1(data):
    safe_report=False
    safe_reports=0
    for report in data.splitlines():
        safe_report=False
        report = report.split()
        report=list(map(int,report))
        if report[0] < report[1]:
            safe_report=ckeck_increasing(report)
        elif report[0] > report[1]:
            safe_report=ckeck_decreasing(report)

        if(safe_report):
            safe_reports+=1
    
    print(safe_reports)

def part2(data):
    pass

def main():
    data=get_data()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()