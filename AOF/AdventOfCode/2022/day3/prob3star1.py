import string
import textwrap

lowerCase = dict.fromkeys(string.ascii_lowercase, 0)
upperCase = dict.fromkeys(string.ascii_uppercase, 0)

index = 1
totSum = 0

for key in lowerCase:
    lowerCase[key] = lowerCase[key] + index
    index = index + 1

for key in upperCase:
    upperCase[key] = upperCase[key] + index
    index = index + 1
   


with open('data3.txt') as f:
    for line in f.readlines():
        comp1, comp2 = textwrap.wrap(line, len(line)//2) #split the line into two equal strings
        comp1 = set(comp1)
        comp2 = set(comp2)
        for ch in comp1:
            if ch in comp2:
                if str(ch).islower():
                    totSum = totSum + lowerCase[ch]
                else: 
                    totSum = totSum + upperCase[ch]
        
    

print(totSum)
