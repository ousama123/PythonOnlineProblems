sum_of_points_in_cards = 0
sum_match = 1
with open('data.txt') as f:
    for line in f.readlines():
        card, lists= line.split(":")
        win_list, my_list= lists.split("|")
        for num in win_list:
            print(num)