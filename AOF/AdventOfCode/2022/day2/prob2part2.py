winRoundScore = 6
lostRoundScore = 0
drawRoundScore = 3

rockScore = 1
paperScore = 2
scissorScore = 3

# A= opponent's Rock
# B= opponent's Paper
# C= opponent's Scissor

# X= my Rock
# Y= my Paper
# Z= my Scissor

myTotalScore = 0
roundScore = 0

with open('data2.txt') as f:
    for line in f.readlines():
        opp, mine = line.split()

        #if mine == "X" and opp == "A": #rock #draw
            #roundScore = drawRoundScore + rockScore
        if opp == "B" and mine == "Y":
            roundScore = drawRoundScore + paperScore
        #if mine == "X" and opp == "C": #rock #win
           # roundScore = winRoundScore + rockScore

        #if mine == "Y" and opp == "A": #Paper #win
            #roundScore = winRoundScore + paperScore
        if opp == "B" and mine == "X":
            roundScore = lostRoundScore + rockScore
        #if mine == "Y" and opp == "C": #paper #lost
            #roundScore = lostRoundScore + paperScore

        #if mine == "Z" and opp == "A": #scissor #lost
            #roundScore = lostRoundScore + scissorScore
        if opp == "B" and mine == "Z":
            roundScore = winRoundScore + scissorScore
        #if mine == "Z" and opp == "C": #scissor #draw
            #roundScore = drawRoundScore + scissorScore

        myTotalScore = myTotalScore + roundScore
    
    print("My total score is: ", myTotalScore)
        

f.close()
