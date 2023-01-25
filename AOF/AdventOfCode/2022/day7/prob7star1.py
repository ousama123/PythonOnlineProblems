totalSize = 0

with open("data7.txt") as f:
    lines = f.readlines()
    for line in lines:
        #if "$" not in line and "dir" not in line:
        split_line = line.split()
        print(split_line)

f.close()