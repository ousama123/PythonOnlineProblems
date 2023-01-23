counter = 0
source=open('output.txt', 'w')
with open("data1.txt") as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        try:
            #print(lines[i+2], file=source)
            if lines[i+1] > lines[i]:
               counter = counter + 1
        except IndexError:
            counter = counter + 1
            pass
    source.close()
    print(counter)