counter = 0
source=open('output.txt', 'w')
with open("data1.txt") as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        try:
            first = lines[i:i+3]
            first = [int(numeric_string) for numeric_string in first]
            second = lines[i+1:i+4]
            second = [int(numeric_string) for numeric_string in second]
            #print(sum(first),"-----------", sum(second), file=source)
            if sum(second) > sum(first):
                counter = counter + 1
        except IndexError:
            pass
    source.close()
    print(counter)