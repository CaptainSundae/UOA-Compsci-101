"""
UPI: jsia894
ID: 8104859
Name: Juan Nicolas Sevilla Siasoco
"""
# Ex 10.5

def print_board(board):
    """ prints out the sudoku board
    Arguments:
        board - the list containing the sudoku board
    Returns:
        nothing
    """
    for i in range(0,9):
        print(str(board[i*9 + 0]) + " " + str(board[i*9+1]) + " " + str(board[i*9+2]) + " " + str(board[i*9+3]) + " " + str(board[i*9+4]) + " " + str(board[i*9+5]) + " " + str(board[i*9+6]) + " " + str(board[i*9+7]) + " " + str(board[i*9+8]))


def calculate(board,i):
    """ returns the numbers which can be placed in this cell
    Arguments:
        i - the index in the list board containing the current cell
        board - the list containing the sudoku board
    Returns:
        list of numbers which can be placed in this cell
    """
    set1 = not_used(get_row(i,board))
    set2 = not_used(get_col(i,board))
    set3 = not_used(get_square(i,board))
    total_set = combine(set1,set2,set3)
    return total_set


def get_col(i,board):
    """ returns the numbers in the column that contains cell i from the sudoku board
    Arguments:
        i - the index in the list board containing the current cell
        board - the list containing the sudoku board
    Returns:
        list of numbers contained in this column of the sudoku board
    """
    start = i % 9
    return board[start:len(board):9]
    

def get_row(i,board):
    """ returns the numbers in the row that contains cell i from the sudoku board
    Arguments:
        i - the index in the list board containing the current cell
        board - the list containing the sudoku board
    Returns:
        list of numbers contained in this row of the sudoku board
    """
    start = i // 9
    num = start*9
    return board[num:num+9]


def get_square(i,board):
    """ returns the numbers in the square that contains cell i from the sudoku board
    Arguments:
        i - the index in the list board containing the current cell
        board - the list containing the sudoku board
    Returns:
        list of numbers contained in this square of the sudoku board
    """
    col = (i % 9) // 3
    row = (i//9) // 3
    start_square = col*3+row*9*3
    return make_square(start_square,board)


def not_used(board):
    """ returns the numbers from 1 - 9 that do not occur in the list calleded board
    Arguments:
        board - the list containing 9 numbers
    Returns:
        list of numbers not contained in this list of 9 numbers
    """
    my_set = []
    for i in range(1,10):
        if i not in board:
            my_set += [i]
    return my_set


def combine(set1, set2, set3):
    """ returns all the numbers that occur in set1 and set2 and set3
    Arguments:
        set1, set2, set3 - a list of numbers
    Returns:
        list of numbers that occur in all 3 lists
    """
    total = []
    for i in range(1,10):
        if i in set1 and i in set2 and i in set3:
            total += [i]
    return total
                

def test_sudoku(board):
    """ returns True or False if the board is a legal Sudoku board
    Arguments:
        board - the list containing the sudoku board
    Returns:
        True or False
    """
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
    """ returns True if 1-9 do not occur more than once in this list
    Arguments:
        my_list - the list of numbers to be tested
    Returns:
        True or False
    """
    for i in range(0,9):
        for num in range (1,10):
            if my_list[i] == num:
                if num in my_list[i+1:]:
                    return False
    return True

def make_square(start,board):
    """ returns the numbers in a square whose top left cell is start from the sudoku board
    Arguments:
        start - the index of the top left cell of a square
        board - the list containing the sudoku board
    Returns:
        list of numbers contained in this square of the sudoku board
    """
    square = []
    for row in range(0,3):
        for col in range(0,3):
            square += [board[start + (row * 9) + col]]
    return square




#Ex 10.6

def find_best_play(person2,storage):
    """returns the choice the computer should make
    Arguments:
        person2 - the choice person2 made
        storage - the dictionary of past plays
    Returns:
        r,p,s whichever is the winning play against the most frequent move of the opponent
    """
    test1 = person2+"r"
    test2 = person2+"p"
    test3 = person2+"s"
    if test1 in storage and test2 in storage and test3 in storage:
        if storage[test1] >= storage[test2] and storage[test1] >= storage[test3]:
            return "p"
        if storage[test2] >= storage[test1] and storage[test2] >= storage[test3]:
            return "s"
        if storage[test3] >= storage[test2] and storage[test3] >= storage[test1]:
            return "r"
    if not test1 in storage and not test2 in storage:
        return "r"
    if not test1 in storage and not test3 in storage:
        return "s"
    if not test2 in storage and not test3 in storage:
        return "p"
    if not test1 in storage and storage[test2] >= storage[test3]:
        return "s"
    if not test1 in storage and storage[test2] <= storage[test3]:
        return "r"
    if not test2 in storage and storage[test1] >= storage[test3]:
        return "p"
    if not test2 in storage and storage[test1] <= storage[test3]:
        return "r"
    if not test3 in storage and storage[test1] >= storage[test2]:
        return "p"
    if not test3 in storage and storage[test1] <= storage[test2]:
        return "s"
        

def find_mapping(person_choice):
    """Returns the index representing the persons choice
    Arguments:
        person_choice - the person's choice, p or s or r
    Returns:
        0 1 2 depending on the person's choice
    """
    mapping = ["p","s","r"]
    for i in range(0,3):
        if person_choice == mapping[i]:
            return i


def who_wins(person1,person2):
    """Returns the name of the person who won, "person1" , "person2" , or "tie"
    Arguments:
        person1 - person1's choice
        person2 - person2's choice
    Returns:
        "person1" or "person2"
    >>> who_wins("rock","scissors")
    'person1'
    >>> who_wins("scissors","paper")
    'person1'
    >>> who_wins("paper","rock")
    'person1'
    >>> who_wins("rock","paper")
    'person2'
    >>> who_wins("scissors","rock")
    'person2'
    >>> who_wins("paper","scissors")
    'person2'
    >>> who_wins("paper","paper")
    'tie'
    """
    if (person1 == "rock" and person2 == "scissors") or (person1 == "scissors" and person2 == "paper") or (person1 == "paper" and person2 == "rock"):
        return "person1"
    elif person1 == person2:
        return "tie"
    return "person2"


def play_sudoku(board):
    """
    Lets you play sudoku.

    Arguement:
    board-- a list containing the sudoku puzzle to solve

    Return:
    A list representing the new board after each attempt.
    """
    print_board(board)
    players_board = board
    game_on = 0
    if game_on == "q":
        return("See you next time!")
    while game_on != "q":
        game_on = input("Enter number or q to quit: ")
        location_row = input("Enter row (0-8): ")
        location_col = input("Enter col (0-8): ")
        co_ordinates = int(location_row) + int(location_col)*9
        if start_board[co_ordinates] == 0:
            if int(game_on) in calculate(board,int(location_row)) and int(game_on) in calculate(board,int(location_col)):
                print("Good choice")
                players_board[co_ordinates] = int(game_on)
                print_board(players_board)

    import doctest
    doctest.testmod()

def play_rock_paper():
    """
    A function that lets you play rock paper scissors with the computer.
    Arguement:

    Return:

    Test:
    >>> play_rock_paper()
    Choose "r" "p" or "s": r
    Computer chose paper.
    You chose rock.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": p
    Computer chose rock.
    You chose paper.
    You win.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": s
    Computer chose rock.
    You chose scissors.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": r
    Computer chose rock.
    You chose rock.
    We are tied.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": p
    Computer chose scissors.
    You chose paper.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": s
    Computer chose rock.
    You chose scissors.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": r
    Computer chose paper.
    You chose rock.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": p
    Computer chose scissors.
    You chose paper.
    Computer wins.

    Do you want to play again? Answer "y" or "n": y
    Choose "r" "p" or "s": s
    Computer chose rock.
    You chose scissors.
    Computer wins.

    Do you want to play again? Answer "y" or "n": n

    """
    import random
    mapping2 = ["paper","scissors","rock"]
    again = "y"
    while again == "y":
        computer_number=random.randint(0,2)
        person2_choice=input('Choose "r" "p" or "s": ')
        person2_num=find_mapping(person2_choice)
        print("Computer chose "+ mapping2[computer_number] +".")
        print("You chose "+mapping2[person2_num]+".")
        winner =who_wins(mapping2[computer_number],mapping2[person2_num])
        if winner == "person2":
            print("You win.")
        elif winner == "tie":
            print("We are tied.")
        else:
            print("Computer wins.")
        again = input('Do you want to play again? Answer "y" or "n": ')

play_rock_paper()



