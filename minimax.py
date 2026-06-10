import math
import random
from connect_four import *

def evaluate_window(window, piece):

    score = 0
    opp_piece = PLAYER

    if piece == PLAYER:
        opp_piece = AI

    if window.count(piece) == 4:
        score += 100

    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10

    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 8

    return score

def score_position(board, piece):

    score = 0

    center_array = [int(i) for i in list(board[:, COLS//2])]
    score += center_array.count(piece) * 3

    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLS - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    for c in range(COLS):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return (
        winning_move(board, PLAYER)
        or winning_move(board, AI)
        or len(get_valid_locations(board)) == 0
    )

def minimax(board, depth, alpha, beta, maximizingPlayer):

    valid_locations = get_valid_locations(board)
    terminal = is_terminal_node(board)

    if depth == 0 or terminal:

        if terminal:

            if winning_move(board, AI):
                return (None, 100000)

            elif winning_move(board, PLAYER):
                return (None, -100000)

            else:
                return (None, 0)

        else:
            return (None, score_position(board, AI))

    if maximizingPlayer:

        value = -math.inf
        column = random.choice(valid_locations)

        for col in valid_locations:

            row = get_next_open_row(board, col)
            temp_board = board.copy()

            drop_piece(temp_board, row, col, AI)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                False
            )[1]

            if new_score > value:
                value = new_score
                column = col

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return column, value

    else:

        value = math.inf
        column = random.choice(valid_locations)

        for col in valid_locations:

            row = get_next_open_row(board, col)
            temp_board = board.copy()

            drop_piece(temp_board, row, col, PLAYER)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                True
            )[1]

            if new_score < value:
                value = new_score
                column = col

            beta = min(beta, value)

            if alpha >= beta:
                break

        return column, value