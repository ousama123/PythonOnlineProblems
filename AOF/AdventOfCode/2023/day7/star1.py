from collections import Counter

def get_data():
    with open("data.txt") as f:
        return f.read()

def get_total_winnings(data):
    for line in data.splitlines():
        hand, bid = line.split()
        print((Counter(hand)))
        

def main():
    data=get_data()
    get_total_winnings(data)

if __name__=="__main__":
    main()