# origingal code
"""i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

	

print "The number: "

for num in numbers:
	print num
"""

def number_loop(z,y):
	i = 0
	numbers = []
	while i < z:
		print "At the top number is %d" % i
		numbers.append(i)

		i = i + y

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "
	for num in numbers:
		print num


print "Give me a number. "
numma = int(raw_input(">> "))
print "What shall we increment by? "
increment = int(raw_input(">> ")) 
number_loop(numma, increment)
