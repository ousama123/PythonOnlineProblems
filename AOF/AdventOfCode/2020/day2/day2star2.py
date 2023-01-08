counter = 0
with open("data2.txt") as f:
    lines = f.readlines()
    for line in lines:
        range, chars, code = line.split()
        char = chars[0]
        if char in code:
            minVal, maxVal = range.split('-')
            minVal = int(minVal) - 1
            maxVal = int(maxVal) - 1

            if (char == code[minVal] and char != code[maxVal]) or (char != code[minVal] and char == code[maxVal]):
                counter = counter + 1
            
                
    print(counter)