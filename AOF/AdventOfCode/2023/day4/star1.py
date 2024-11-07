
def get_data():
    with open('data.txt') as f:
        return f.read()

def calculate_points(matches):
    points= 0
    if matches == 1:
        return 1
    elif matches == 0:
        return 0
    else:
        points = 1
        for _ in range(1, matches):
            points *=2
    return points

def star1(data):
    cards= data.split("\n")
    num_of_matches = 0
    total_points = 0
    for card in cards:
        card_num, numbers = card.strip().split(":")
        win_nums, my_nums=numbers.split("|")
        win_nums=set(win_nums.split())
        my_nums= set(my_nums.split())
        if (win_nums.intersection(my_nums)):
            num_of_matches = len(win_nums.intersection(my_nums))
            points = calculate_points(num_of_matches)
            total_points +=points 
    print(f"total points: {total_points}")


if __name__ == "__main__":
    data = get_data()
    star1(data)
    #star2(data)        