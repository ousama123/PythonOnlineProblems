hrztl = 0
depth = 0
aim = 0

with open("data2.txt") as f:
    lines = f.readlines()
    for line in lines:
        command, val = line.split()
        val =int(val)

        if command == "forward":
            hrztl = hrztl + val
            depth = depth + (aim * val)
        
        if command == "down":
            aim = aim + val
        
        if command == "up":
            aim = aim - val
    
    print(depth*hrztl)
    f.close()
