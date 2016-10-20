# asks the user how many Fibonnaci numbers to generate and then generates them
# a sequence of numbers where the next number in the sequence 
# is the sum of the previous two numbers (1, 1, 2, 3, 5, 8, etc)

def fibo(num):
	seq = [1, 1]

	while (len(seq) <= num - 1):
		seq.append(seq[-1] + seq[-2])
	
	return seq

digits = int(raw_input("How many Fibonacci numbers do you want?"))

print(fibo(digits))


    