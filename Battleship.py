#!/usr/bin/env python
from random import randint

# initialise variables
board = []
maxturns = 5

# fill board with 0 representing water
for x in range(5):
    board.append(["0"] * 5)


###### FUNC to print the board to the screen
def print_board(board):
    for row in board:
        print " ".join(row)


# introduction
print "Let's play Battleship!"
print_board(board)


# ----- set battleship position -----
def random_col(board):
    return randint(0, len(board) - 1)


def random_row(board):
    return randint(0, len(board) - 1)


# set location of battleship
ship_row = random_row(board)
ship_col = random_col(board)

# ---------- GAMEPLAY --------- #
for turn in range(1, maxturns + 1):
    # turn title
    print "=== Turn %s ===" % turn

    # get player input
    guess_col = int(raw_input("Guess Col: ")) - 1
    guess_row = int(raw_input("Guess Row: ")) - 1

    # check the guess
    if guess_col == ship_col and guess_row == ship_row:
        board[guess_row][guess_col] = "B"
        print_board(board)
        print "You found the ship!"
        break
    elif guess_col < 0 or guess_row < 0 or guess_col + 1 > 5 or guess_row + 1 > 5:
        print "That's off the board..."
    elif board[guess_row][guess_col] == "X":
        print "You already guessed that one!"
    else:
        print "You missed!"
        board[guess_row][guess_col] = "X"

    # conclude the turn
    if maxturns - turn == 0:
        print "You lost!"
        # make ship visible for fairness
        board[ship_row][ship_col] = "B"
    else:
        print "You have %s turns left." % (maxturns - turn)

    print_board(board)
