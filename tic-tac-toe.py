# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:45:19 2024

@author: MEDHA TRUST
"""


import random

# Game board
board = [' ' for _ in range(9)]

# Function to draw the game board
def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle player move
def player_move(icon):
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

# Function to handle AI move
def ai_move(icon):
    possible_moves = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(possible_moves)
    board[move] = icon

# Function to check for a win
def check_win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Main game loop
while True:
    draw_board()
    player_move('X')
    draw_board()
    if check_win('X'):
        print("Player 1 wins! Congratulations!")
        break
    ai_move('O')
    draw_board()
    if check_win('O'):
        print("AI wins!")
        break
'''
runfile('C:/Users/MEDHA TRUST/untitled0.py', wdir='C:/Users/MEDHA TRUST')

|   |   |   |
|   |   |   |
|   |   |   |

Enter your move (1-9): 5

|   |   |   |
|   | X |   |
|   |   |   |


|   |   | O |
|   | X |   |
|   |   |   |


|   |   | O |
|   | X |   |
|   |   |   |

Enter your move (1-9): 2

|   | X | O |
|   | X |   |
|   |   |   |


|   | X | O |
| O | X |   |
|   |   |   |


|   | X | O |
| O | X |   |
|   |   |   |

Enter your move (1-9): 8

|   | X | O |
| O | X |   |
|   | X |   |

Player 1 wins! Congratulations!
'''
