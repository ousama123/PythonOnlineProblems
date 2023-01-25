
def main(visible,current):
    with open("data8.txt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            for j in range(len(lines)):
                if i == 0 or j == 0 or i == len(lines)-1 or j == len(lines)-1: #counting the edges
                    visible +=1
                current = lines[i][j]
                visible =  check_same_row_col(current,i,j,lines,visible)
        return visible

def check_same_row_col(current,i,j,lines,visible):
    for k in range(len(lines)):
        if current < lines[i][k] and current < lines[k][j]:
            visible +=1
    return visible

if __name__=="main":
    visible = 0
    current = 0
    visible=main(visible)
    print(visible)
            


