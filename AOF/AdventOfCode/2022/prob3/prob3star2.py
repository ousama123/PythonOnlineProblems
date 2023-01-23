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
   

f = open("data3.txt", 'r')
lines = f.readlines()
for i in range(0, len(lines), 3):
    line1 = set(lines[i].strip())
    line2 = set(lines[i+1].strip())
    line3 = set(lines[i+2].strip())
    for ch in line1:
            if ch in line2 and ch in line3:
                if str(ch).islower():
                    totSum = totSum + lowerCase[ch]
                else: 
                    totSum = totSum + upperCase[ch]

print(totSum)                    


        
