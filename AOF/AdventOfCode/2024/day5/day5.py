from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()
    
def check_rule(rules, page1, page2):
    for rule in rules.splitlines():
        left_num, right_num = list(map(int, rule.split('|')))
        if page1 == (left_num) and page2 == (right_num):
            return True
    return False

def part1(rules, updates):
    cnt_updates = 0
    all_pages = []
    for update in updates.splitlines():  
        all_pages = []      
        update = list(map(int,update.split(",")))
        for page_i in range(len(update)):
            for page_j in range(page_i+1, len(update)):
                if page_i+1 == len(update):
                    all_pages.append(True)                    
                all_pages.append((check_rule(rules, update[page_i], update[page_j])))

        if all(all_pages):
            mid_index = (len(update)//2)
            cnt_updates += update[mid_index]               
    
    print(cnt_updates)

def main():
    data=get_data()
    rules, updates = data.split('\n\n')
    part1(rules, updates)
    

if __name__ == "__main__":
    main()