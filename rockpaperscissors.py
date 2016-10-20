# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), 
# compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

def RockPaperScissors_AI (hand1, hand2):
	if hand1 == hand2:
		print("It's a draw!")
		return

	if hand1 == "rock" and hand2 == "paper":
		print("Player 2 wins!")
	elif hand1 == "rock" and hand2 == "scissors":
		print("Player 1 wins!")
	elif hand1 == "paper" and hand2 == "rock":
		print("Player 1 wins!")
	elif hand1 == "paper" and hand2 == "scissors":
		print("Player 2 wins!")
	elif hand1 == "scissors" and hand2 == "paper":
		print("Player 1 wins!")
	elif hand1 == "scissors" and hand2 == "rock":
		print("Player 2 wins!")
	else:
		print("Who won?!")

# list for allowed input to check against
allowed_input = ["rock", "paper", "scissors"]

while True:
	# take input for player 1
	p1_play = raw_input("Player 1 Hand: \n")
	while (p1_play not in allowed_input):
		print("Please enter 'rock', 'paper', or 'scissors'.\n")
		p1_play = raw_input("Player 1 Hand: \n")

	# take input for player 2
	p2_play = raw_input("Player 2 Hand: \n")
	while (p2_play not in allowed_input):
		print("Please enter 'rock', 'paper', or 'scissors'.\n")
		p2_play = raw_input("Player 2 Hand: \n")

	# compare plays to determine winner
	RockPaperScissors_AI(p1_play, p2_play)

	# ask if they want to start a new game
	choice = raw_input("Do you want to play again? Y/N")

	# terminate
	if choice == "N":
		break