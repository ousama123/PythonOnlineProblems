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

def check_safe_report(report):
    safe_report= False
    if report[0] < report[1]:
        safe_report=ckeck_increasing(report)
    elif report[0] > report[1]:
        safe_report=ckeck_decreasing(report)
    
    return safe_report

def part1(data):
    safe_report=False
    safe_reports=0
    for report in data.splitlines():
        safe_report=False
        report = report.split()
        report=list(map(int,report))
        safe_report=check_safe_report(report)
        if(safe_report):
            safe_reports+=1
    
    print(safe_reports)

def part2(data):
    safe_report=False
    safe_reports=0
    for report in data.splitlines():
        safe_report=False
        report = report.split()
        report=list(map(int,report))

        safe_report= check_safe_report(report)
        
        if not safe_report:
            for idx in range(len(report)):
                new_report=report[:idx] + report[idx+1:]
                safe_report=check_safe_report(new_report)
                
                #break the loop once you get at least one safe report
                if(safe_report):                    
                    break
        
        if safe_report:
            safe_reports +=1
    
    print(safe_reports)

def main():
    data=get_data()
    #part1(data)
    part2(data)

if __name__ == "__main__":
    main()