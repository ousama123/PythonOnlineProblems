hrztl = 0
depth = 0

with open("data2.txt") as f:
    lines = f.readlines()
    for line in lines:
        command, val = line.split()
        val =int(val)

        if command == "forward":
            hrztl = hrztl + val
        
        if command == "down":
            depth = depth + val
        
        if command == "up":
            depth = depth - val
    
    print(depth*hrztl)
    f.close()
