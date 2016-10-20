# Ask the user for a string and print out whether this string is a palindrome or not.

# ask user for a string
string = raw_input("Please give me a string to check:")

# check for palindrome
def isPalindrome(string):
	rev = string[::-1]

	if rev == string:
		return True
	else:
		return False

# check and display
if isPalindrome(string):
	print("The string is a palindrome")
else:
	print("The string is not a palindrome")