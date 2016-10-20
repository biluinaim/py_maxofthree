# take two lists of different sizes
# return a list contains only the common elements

# extra: randomly generate the lists
import random

def list_overlap (list1, list2):
	result = []

	# add members of list 1 to result if they're alson in list2
	for elem in list1:
		if elem in list2 and elem not in result:
			result.append(elem)

	return result

# generate random lists
a = []
b = []
random.seed()

i = 0
rndrng1 = random.randint(0, 20)
while (i <= rndrng1):
	a.append(random.randint(0, 20))
	i += 1

rndrng2 = random.randint(0, 20)
z = 0
while (z <= rndrng2):
	b.append(random.randint(0, 20))
	z += 1

res = list_overlap(b, a)

print res