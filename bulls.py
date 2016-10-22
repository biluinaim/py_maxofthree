# generate a random 4 digit number
# user enters a guess
# if right digit in right place = cow
# if right digit in wrong place = bull

# extra: keep count of attempts and display to user

import random


def compare(answer, guess):
	# counter for cows and bulls
	cowbull = [0, 0] 

	# convert data to string for ease of iteration
	answer = str(answer)
	guess = str(guess)

	# compare the digits and count cows and bulls
	i = 0
	while (i <= 3):
		if guess[i] == answer[i]:
			cowbull[0] += 1
		else:
			cowbull[1] += 1
		i += 1

	return cowbull


if __name__ == "__main__":

	# set up variables
	playing = True
	number = str(random.randint(1000, 9999))
	guesses = 0

	# DEBUG
	print(number)

	while playing:
		# take user input
		guess = int(input("Your guess: "))

		# check for exit cue
		if guess == "exit":
			break

		# compare guess to solution
		result = compare(number, guess)
		guesses += 1

		# react to the result
		# when we get 4 cows
		if result[0] == 4:
			print("Congratulations!\n")
			print("It took you " + str(guesses) + " guesses.")
			playing = False
			break
		else:
			# show us cow/bull count
			print(str(result[0]) + " cows, " + str(result[1]) + " bulls.")

