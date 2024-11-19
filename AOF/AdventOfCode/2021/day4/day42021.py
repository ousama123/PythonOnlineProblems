class Value:
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
            for col_idx, col in enumerate(row.split()):
                col=int(col)
                parsed_board.append(Value(col, (row_idx,col_idx)))
        
        return parsed_board


def get_data():
    with open(r'C:\Users\oussama.anadani\Desktop\PythonOnlineProblems\AOF\AdventOfCode\2021\day4\data.txt') as f:
        return f.read()
    
def main():
    data=get_data()
    numbers, *boards=data.split('\n\n')
    numbers=list(map(int,numbers.split(",")))
    
    fixed_boards=[Board(board, idx) for idx, board in enumerate(boards)]

    for number in numbers:
        for board in fixed_boards:
            for element in board.parsed_board:
                if number == element.value:
                    element.marked= True
    
    print([ele.marked for ele in board.parsed_board])

if __name__=="__main__":
    main()