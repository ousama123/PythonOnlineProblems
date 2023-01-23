
stack1 = ["J","H","G","M","Z","N","T","F"]
stack2 = ["V","W","J"]
stack3 = ["G","V","L","J","B","T","H"]
stack4 = ["B","P","J","N","C","D","V","L"]
stack5 = ["F","W","S","M","P","R","G"]
stack6 = ["G","H","C","F","B","N","V","M"]
stack7 = ["D","H","G","M","R"]
stack8 = ["H","N","M","V","Z","D"]
stack9 = ["G","N","F","H"]

stackDict ={
1:stack1,
2:stack2,
3:stack3,
4:stack4,
5:stack5,
6:stack6,
7:stack7,
8:stack8,
9:stack9}

testDict={1:stack9}

counter = 0

digitsList = []

with open("data5.txt") as f:
    lines = f.readlines()
    for line in lines:
        splitLine = line.split() #split line between spaces
        
        if ("move" and "from" and "to") in splitLine: #skip the first few lines which contain the stacks and getting the wanted lines which contain move, from and to
            for ch in splitLine:
                if ch.isdigit():
                    digitsList.append(int(ch))

            steps, fromListNr, toListNr = digitsList
            for step in range(0, steps):
                if fromListNr in stackDict.keys() and toListNr in stackDict.keys():
                    stackDict[toListNr].append(stackDict[fromListNr].pop())
            
        digitsList.clear()

    print("Whole stack: ", stackDict)
    print("Top containers: ", stackDict[1].pop(), stackDict[2].pop(),stackDict[3].pop(),stackDict[4].pop(),stackDict[5].pop(),stackDict[6].pop(),stackDict[7].pop(),stackDict[8].pop(),stackDict[9].pop())
   

        #arr.clear()

