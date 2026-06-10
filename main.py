import pygame
import sys
import math

from connect_four import *
from minimax import minimax

pygame.init()

SQUARESIZE = 100

width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE

size = (width, height)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four AI")

font = pygame.font.SysFont("monospace", 60)

board = create_board()

def draw_board(board):

    for c in range(COLS):
        for r in range(ROWS):

            pygame.draw.rect(
                screen,
                BLUE,
                (c*SQUARESIZE,
                 (r+1)*SQUARESIZE,
                 SQUARESIZE,
                 SQUARESIZE)
            )

            pygame.draw.circle(
                screen,
                BLACK,
                (
                    int(c*SQUARESIZE+SQUARESIZE/2),
                    int((r+1)*SQUARESIZE+SQUARESIZE/2)
                ),
                40
            )

    for c in range(COLS):
        for r in range(ROWS):

            if board[r][c] == PLAYER:

                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        int(c*SQUARESIZE+SQUARESIZE/2),
                        height-int(r*SQUARESIZE+SQUARESIZE/2)
                    ),
                    40
                )

            elif board[r][c] == AI:

                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (
                        int(c*SQUARESIZE+SQUARESIZE/2),
                        height-int(r*SQUARESIZE+SQUARESIZE/2)
                    ),
                    40
                )

    pygame.display.update()

draw_board(board)

turn = 0
game_over = False

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if turn == PLAYER:

                col = event.pos[0] // SQUARESIZE

                if is_valid_location(board, col):

                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER)

                    if winning_move(board, PLAYER):
                        label = font.render(
                            "You Win!",
                            True,
                            RED
                        )
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn = AI

                    draw_board(board)

    if turn == AI and not game_over:

        col, score = minimax(
            board,
            5,
            -math.inf,
            math.inf,
            True
        )

        if is_valid_location(board, col):

            row = get_next_open_row(board, col)

            drop_piece(board, row, col, AI)

            if winning_move(board, AI):
                label = font.render(
                    "AI Wins!",
                    True,
                    YELLOW
                )
                screen.blit(label, (40, 10))
                game_over = True

            draw_board(board)

            turn = PLAYER

    if game_over:
        pygame.time.wait(5000)