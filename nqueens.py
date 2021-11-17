class QueenChessBoard:
    def __init__(self, size):
        # dimensionet e tabeles size x size
        self.size = size
        self.columns = []
 
    def get_size(self):
        return self.size
 
    def get_queens_count(self):
        return len(self.columns)
 
    def place_in_next_row(self, column):
        self.columns.append(column)
 
    def remove_in_current_row(self):
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column):
        # index i rreshtit te ardhshem
        row = len(self.columns)
 
        # kontrollo kolonen
        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        # kontrollo diagonalen
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
        # kontrollo diagonalen tjeter
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
 
    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
 
 
def print_all_solutions_to_n_queen(size):
   
    board = QueenChessBoard(size)
    number_of_solutions = print_all_solutions_helper(board)
    print('Numri i zgjidhjeve: ', number_of_solutions)
 
def print_all_solutions_helper(board):
  
    size = board.get_size()
 
    # nese tabela mbushet shfaq zgjidhjen
    if size == board.get_queens_count():
        board.display()
        print()
        return 1
 
    number_of_solutions = 0
    # vendos mbretereshen ne rreshtin e ardhshem
    for column in range(size):
        if board.is_this_column_safe_in_next_row(column):
            board.place_in_next_row(column)
            number_of_solutions += print_all_solutions_helper(board)
            board.remove_in_current_row()
 
    return number_of_solutions
 
 
n = int(input('Jep madhesine e tabeles: '))
# numri i n qe e japim percakton edhe numrin e mbretereshave
print_all_solutions_to_n_queen(n)
