#!/usr/bin/env python


# function that returns the max out of 3 numbers
def max_num (num1, num2, num3):
	if (num1 >= num2) and (num2 >= num3):
		return num1
	elif (num2 >= num3) and (num2 >= num1):
		return num2
	elif (num3 >= num1) and (num3 >= num2):
		return num3


# take 3 numbers as input
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# find the result
res = max_num(num1, num2, num3)

# print highest of the 3 
print("The highest of the 3 is: " + str(res))


