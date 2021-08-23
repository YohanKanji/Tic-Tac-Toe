import numpy as np
import random 
random.seed(1)

def create_board():
    emptyBoard = np.zeros((3,3), dtype = int)
    return emptyBoard

def place(board, player, position):
    if player == 1 or player == 2:
        if board[position] == 0:
            board[position] = player
            return board
        else:
            print('Position Unavailable')
            print('The Possibilities are:',possibilities(board))
            return board
    else:
        print('Error - Invalid Player Number')
    
def possibilities(board):
    x=zip(*np.where(board == 0))
    global y
    y=list(x)
    return y

def random_place(board, player):
    if player == 1 or player == 2:
        available = possibilities(board)
        place(board, player, random.choice(available))
        return board
    else:
        print('Error - Invalid Player Number')
    
def row_win(board, player):
    if player == 1 or player == 2:
        for row in board:
            if check_row(row, player):
                return True
        return False
    else:
        print('Error - Invalid Player Number')
        
def col_win(board, player):
    if player == 1 or player == 2:
        return (board==[player]).all(axis=0)
    else:
        print('Error - Invalid Player Number')

def check_row(row, player):
    if player == 1 or player == 2:
        for marker in row:
            if marker != player:
                return False
        return True
    else:
        print('Error - Invalid Player Number')
        
def col_win(board, player):
    for col in board.T:
        if check_win(col, player):
            return True
    return False

def diag_win(board, player):
    main_diag = board.diagonal()
    anti_diag = np.flipud(board).diagonal()[::-1]
    return check_win(main_diag, player) or check_win(anti_diag, player)        


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) == True or col_win(board, player) == True or diag_win(board, player) == True:
            winner = player
            return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) == True or col_win(board, player) == True or diag_win(board, player) == True:
            winner = player
            return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result
            
board = create_board()
print(board)

