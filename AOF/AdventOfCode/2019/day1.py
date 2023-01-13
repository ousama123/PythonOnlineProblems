sum=0
with open("data1.txt") as f:
    lines= f.readlines()
    for line in lines:
        sum+=int(int(line)/3)-2
    print(sum)