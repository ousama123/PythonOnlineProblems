sections1List = []
sections2List = []
counter = 0


with open("data4.txt") as f:
    lines = f.readlines()
    print("file length: ", len(lines))
    for line in lines:
        sec1,sec2 = line.split(",")
        sec1Start, sec1End = sec1.split("-")
        sec2Start, sec2End = sec2.split("-")
        sec1Start, sec1End, sec2Start, sec2End = int(sec1Start), int(sec1End), int(sec2Start), int(sec2End)

        for i in range(sec1Start, sec1End+1):
            sections1List.append(i)
        for i in range(sec2Start, sec2End+1):
            sections2List.append(i)

         #check if there is any overlap 
        check =  any(item in sections1List for item in sections2List)
        if check is True:
            counter = counter + 1

        sections1List.clear()
        sections2List.clear()

print("count: ", counter)