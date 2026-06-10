import numpy as np

ROWS = 6
COLS = 7

EMPTY = 0
PLAYER = 1
AI = 2

def create_board():
    return np.zeros((ROWS, COLS))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROWS - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def get_valid_locations(board):
    valid = []
    for col in range(COLS):
        if is_valid_location(board, col):
            valid.append(col)
    return valid

def winning_move(board, piece):

    for c in range(COLS - 3):
        for r in range(ROWS):
            if (board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece):
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece):
                return True

    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece):
                return True

    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if (board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece):
                return True

    return False