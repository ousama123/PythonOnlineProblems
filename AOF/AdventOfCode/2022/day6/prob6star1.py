marker = False

with open("data6.txt") as f:
    lines = f.readlines()
    for line in lines:
        for i in range(0, len(line)):
            sub = line[i:i+14] # line[i:i+4] for star 1
            if len(set(sub)) == len(sub):
                marker = True      
            if marker:
                print(sub)
                print(i+14) # print(i+4) for star 1
                break
     
f.close()