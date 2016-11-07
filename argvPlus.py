from sys import argv

fruit1, fruit2, fruit3, fruit4, fruit5 = argv

partialToFruit = raw_input("Do you like fruit? ")

if partialToFruit == "yes":

	# print "First fruit is: ", fruit1
	print "First fruit is: ", fruit2
	print "First fruit is: ", fruit3
	print "First fruit is: ", fruit4
	print "First fruit is: ", fruit5

print "I would guess that your favourite fruit is %s" % fruit4
