games= []
sum_valid_game_IDs = 0

REDS_ = 12
GREENS_ = 13
BLUES_ = 14

list_blues=[]
list_reds=[]
list_greens=[]
sum_of_power = 0

with open('data23.txt') as f:
    for line in f.readlines():
        game_number, game_set = line.split(":")
        _, id_ = game_number.split()
        id_ = int(id_)
        games.append((id_, [line for line in game_set.split("\n") if line]))
    for game in games:
        list_blues=[]
        list_reds=[]
        list_greens=[]
        id_, subs = game
        for sub in subs:
            sub=sub.split(';')
            for subSub in sub:
                subSub= subSub.split(',')
                for subsubsub in subSub:
                    cube_count, cube_color = subsubsub.split()
                    cube_count = int(cube_count)

                    if cube_color == 'blue':
                        list_blues.append(cube_count)
                    if cube_color == 'red':
                        list_reds.append(cube_count)
                    if cube_color=='green':
                        list_greens.append(cube_count)
        #print(list_greens)
        #print(list_blues)
        #print(list_reds)
        sum_of_power += max(list_greens) * max(list_blues) * max(list_reds)
        #print("power: ", power)        
        #sum_of_power += power
    print("sum_of_power: ", sum_of_power)



                        

