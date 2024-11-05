games= []
sum_valid_game_IDs = 0

REDS_ = 12
GREENS_ = 13
BLUES_ = 14

total_blues=0
total_reds=0
total_greens=0

with open('data23.txt') as f:
    for line in f.readlines():
        game_number, game_set = line.split(":")
        _, id_ = game_number.split()
        id_ = int(id_)
        games.append((id_, [line for line in game_set.split("\n") if line]))

    for game in games:        
        id_, subs = game
        valid_game = True

        for sub in subs:
            sub=sub.split(';')
            for subSub in sub:
                subSub= subSub.split(',')
                for subsubsub in subSub:
                    cube_count, cube_color = subsubsub.split()
                    cube_count = int(cube_count)

                    if ((cube_color == 'blue' and cube_count > BLUES_) or (cube_color == 'red' and cube_count > REDS_) or (cube_color=='green' and cube_count > GREENS_)):
                        valid_game = False
                        break
                if not valid_game:
                    break
            if not valid_game:
                break

        if valid_game:
            sum_valid_game_IDs +=id_        

    print(sum_valid_game_IDs)
                        

