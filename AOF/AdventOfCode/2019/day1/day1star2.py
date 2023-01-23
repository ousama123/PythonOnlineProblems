
total= 0
num=0
with open("data1.txt") as f:
    lines= f.readlines()
    for line in lines:
        num=0
        num=int(int(line)/3)-2
        while num > 0:
            total+=num
            num=int(int(num)/3)-2
            
    print(total)
            
