def dest_choice(a):
	if a == "jungle":
		jungle()
	elif a == "mountain":
		mountain()
	elif a == "swamp":
		swamp()
	else:
		print "%s can't see that, %s decides to pick one of the 3 available." % name
		first_choice()
		dest_choice(destination)

def jungle():
	print "jungle"

def mountain():
	print "mountain"

def swamp():
	print "swamp"



print """An adventurer of mild manner and poor judgement lands on the shores of the newly discovered island of Whitestone. It is an ominous place, bringing forth a sense of foreboding.
Our adventurer is here to chart the island of its landscape and fauna, the general consensus is still undecided if he is brave or stupid.\n"""

name = raw_input("What was his name name again? ")

print "A of course, how could I forget. %s is such a strong name. " % name

print "After landing on the beach " + name + " waves goodbye to the ship he disembarked from, it set sail as soon as he had gotten off - they did not want to hang around.\n"

def first_choice():
	print "He scanned his horizon and saw 3 options;\n\t* jungle\n\t* mountain\n\t* swamp\n" + name + " thinks about it breifly but then decides "
	global destination
	destination = raw_input(" ")

first_choice()

dest_choice(destination)
