class Cell:
    def __init__(self, value: int, position: tuple):
        self.marked= False
        self.value = value
        self.position= position

class Board:
    def __init__(self, board, idx):
        self.idx=idx
        self.parsed_board = self.parse_board(board)
    
    def parse_board(self, board):
        parsed_board=[]
        for row_idx, row in enumerate(board.splitlines()):
            parsed_board.append([Cell(int(col), (row_idx, col_idx)) for col_idx, col in enumerate(row.split())])

        return parsed_board

    def check_bingo(self):
        for row in self.parsed_board:            
            if all(cell.marked for cell in row):
                return True
        
        for col in zip(*self.parsed_board): # generate a transposed matrix 
            if all(cell.marked for cell in col):
                return True

        return False
    
    def calculate_score(self, num):
        unmarked_values=[]
        for row in self.parsed_board:
            [unmarked_values.append(cell.value) for cell in row if cell.marked == False] 
        
        score = sum(unmarked_values) * num
        return score
    

def get_data():
    with open(r'C:\Users\oussama.anadani\Desktop\PythonOnlineProblems\AOF\AdventOfCode\2021\day4\data.txt') as f:
        return f.read()

def star1(numbers, fixed_boards):
    for number in numbers:
        for board in fixed_boards:
            for row in board.parsed_board:
                for cell in row:
                    if cell.value == number:
                        cell.marked= True
        
            if(board.check_bingo()):
                print(f"Bingo board index: {board.idx}")
                print(f"Score: {board.calculate_score(number)}")
                return

def main():
    data=get_data()
    numbers, *boards=data.split('\n\n')
    numbers=list(map(int,numbers.split(",")))
    
    fixed_boards=[Board(board, idx) for idx, board in enumerate(boards)]
    star1(numbers,fixed_boards)

    #print([ele.value for ele in board.parsed_board if ele.marked])

if __name__=="__main__":
    main()