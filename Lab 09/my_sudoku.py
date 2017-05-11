def get_col(i,board):
    start = i % 9
    return board[start:len(board):9]
    

def get_row(i,board):
    start = i // 9
    num = start*9
    return board[num:num+9]

def get_square(i,board):
    col = (i % 9) // 3
    row = (i//9) // 3
    start_square = col*3+row*9*3
    return make_square(start_square,board)

def not_used(board):
    my_set = []
    for i in range(1,10):
        if i not in board:
            my_set += [i]
    return my_set

def combine(set1, set2, set3):
    total = []
    for i in range(1,10):
        if i in set1 and i in set2 and i in set3:
            total += [i]
    return total
    


            

def test_sudoku(board):
    for i in range(0,9):
        col = board[i:len(board):9]
        if not test(col):
            return False
        row = board[i*9:(i*9)+9]
        if not test(row):
            return False
    for column in range(0,3):
        for row in range(0,3):
            start_square = column*3+row*9*3
            square = make_square(start_square,board)
            if not test(square):
                return False
    return True

def test(my_list):
    for i in range(0,9):
        for num in range (1,10):
            if my_list[i] == num:
                if num in my_list[i+1:]:
                    return False
    return True

def make_square(start,board):
    square = []
    for row in range(0,3):
        for col in range(0,3):
            square += [board[start + (row * 9) + col]]
    return square
