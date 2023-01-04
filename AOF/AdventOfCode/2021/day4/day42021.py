
from collections import defaultdict
import numpy as np
data=defaultdict()
marked = False
matrix=[]
final_matrix = []
with open("data4.txt") as f:
    lines = f.readlines()
    for i in range(0,len(lines)):
        #lines[i] = int(str(lines[i]))
        if i==0:
            values=lines[i].split(',')
            for j in values:
                data[int(j)] = marked

        if lines[i] != "\n" and i != 0:
            #a new matrix approached
            line = (lines[i].split())
            matrix.append(line)

    print("bo")
    print(matrix)    
    
            



    
        

        
            
    
    