# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

sentence = raw_input("Give me a sentence: \n")
print(' '.join(sentence.split()[::-1]))

