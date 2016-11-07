# define the chees & crackers function - passing in 2 arguments 'cheese_count' & 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# pass in 2 numbers directly to the function - 20 for cheese_count & 30 for boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# pass in values stored in a variable to the function - amount_of_cheese for cheese_count & amount_of_crackers for boxes_of_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# pass in math directly to each argument of the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 30, 5 + 16)

# pass in the variable value + some math for the arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
