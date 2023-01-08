counter = 0
with open("data2.txt") as f:
    lines = f.readlines()
    for line in lines:
        freq = 0
        range, chars, code = line.split()
        char = chars[0]
        if char in code:
            minVal, maxVal = range.split('-')
            for char1 in code:
                if char1 == char:
                    freq = freq +1
            if freq >= int(minVal) and freq <= int(maxVal):
                counter = counter + 1
    
    print(counter)