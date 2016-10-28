# 
# BUGS: 

# 1. If the board is full after P1 plays, P2 is stuck forever
# 2. FIXED - What is "none" being drawn when checking for result?
# 3. FIXED - Crash when inputting coords out of range
# 4. FIXED? - P1 and P2 can win at the same time because wincheck is only after both
# 5. Game should quit after a winner is found
# 6. Game ends with no notice sometimes when board isn't full

def draw_board(board):

	print("     |    |    ")
	print(' ' +str(board[0][0])+ '   | ' +str(board[0][1])+ '  | ' +str(board[0][2]))
	print("     |    |    ")
	print('---------------')
	print("     |    |    ")
	print(' ' +str(board[1][0])+ '   | ' +str(board[1][1])+ '  | ' +str(board[1][2]))
	print("     |    |    ")
	print('---------------')
	print("     |    |    ")
	print(' ' +str(board[2][0])+ '   | ' +str(board[2][1])+ '  | ' +str(board[2][2]))
	print("     |    |    ")

def take_player_move(player):
	choice = []

	input = raw_input("P" + str(player) + ": enter your move. \n")
	choice = input.split(",")
	while (len(choice) != 2):
		input = raw_input("P" + str(player) + ": enter your move. \n")
		choice = input.split(",")

	# adjust for player starting at 1 instead of 0
	choice[0] = int(choice[0]) - 1
	choice[1] = int(choice[1]) - 1

	return choice

def legal_move(move, board):

	canMove = True
	
	# check for out of range
	if move[0] > 3 or move[1] > 3:
		canMove = False

	# check if position is occupied
	elif (board[move[0]][move[1]] != 0):
		canMove = False

	# return boolean
	return canMove

def make_move(move, board, player):
	board[move[0]][move[1]] = int(player)

	# draw the board
	draw_board(board)


def calc_solution(board):
	win = False

	# vertical wins
	for x in range(3):
		if (board[0][x] == board[1][x] == board[2][x] and
			board[0][x] != 0):
			print("Player {} wins!".format(board[0][x]))
			win = True

	# horizontal wins
	for x in range(3):
		if (board[x][0] == board[x][1] == board[x][2] and
			board[x][0] != 0):
			print("Player {} wins!".format(board[x][0]))
			win = True

	# diagonal wins
	if (board[0][0] == board[1][1] == board[2][2] and
		board[0][0] != 0):
		print("Player {} wins!".format(board[0][0]))
		win = True
	elif (board[0][2] == board[1][1] == board[2][0] and
		board[0][2] != 0):
		print("Player {} wins!".format(board[0][2]))
		win = True

def player_turn(player, board):
	move = take_player_move(player)

	while (not legal_move(move, board)):
		print("You can't make this move.")
		move = take_player_move(player)

	make_move(move, board, player)

def game_over(board):
	
	full_board = False

	# check for full board and call a draw
	for x in range(3):
		for y in range(3):
			if board[x][y] != 0:
				full_board = True
			else:
				full_board = False

	if (full_board):
		return True
	else:
		return False


if __name__ == "__main__":

	# initialise
	win = False
	board = [ [0, 0, 0], 
			  [0, 0, 0],
			  [0, 0, 0] ]

	# TODO game instructions
	print(draw_board(board))

	while not win and not game_over(board):

		# == take player 1 move
		player = 1
		player_turn(player, board)
		calc_solution(board)

		# == take player 2 move
		player = 2
		player_turn(player, board)
		calc_solution(board)

	#if (game_over(board)):
	#	print("It's a draw!")

