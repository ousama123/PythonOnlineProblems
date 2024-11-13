grid = []
list_of_numbers = []
valid_numbers = []

def isValid(i,j,grid):
    start = len(grid)
    end = len(grid[0])
    if i<0 or j <0 or i >=start or j >= end:
        return False
    return True

def hasSymbolAdj(i,j,grid):
    list_valid_adjacents=[]

    if isValid(i-1,j-1,grid):
        list_valid_adjacents.append(str(grid[i-1][j-1]))
    if isValid(i-1,j,grid):
        list_valid_adjacents.append(str(grid[i-1][j]))
    if isValid(i,j-1,grid):
        list_valid_adjacents.append(str(grid[i][j-1]))
    if isValid(i+1,j-1,grid):
        list_valid_adjacents.append(str(grid[i+1][j-1]))
    if isValid(i+1,j,grid):
        list_valid_adjacents.append(str(grid[i+1][j]))
    if isValid(i+1,j+1,grid):
        list_valid_adjacents.append(str(grid[i+1][j+1]))
    if isValid(i,j+1,grid):
        list_valid_adjacents.append(str(grid[i][j+1]))
    if isValid(i-1,j+1,grid):
        list_valid_adjacents.append(str(grid[i-1][j+1]))  

    for item in list_valid_adjacents:
        if not str(item).isalnum() and item != '.':
            return True
    return False  

with open("data.txt") as f:
    for line in f.readlines():
        number_has_symbol_adj = False 
        grid.append(line.strip()) 
    for i in range(len(grid)):
        for j in range(len(grid[0])):            
            current_element = str(grid[i][j])
            #TODO
            
        