def dest_choice(a):
	if a == "jungle":
		jungle()
	elif a == "mountain":
		mountain()
	elif a == "swamp":
		swamp()
	else:
		print "%s can't see that, %s decides to pick one of the 3 available." % (name, name)
		first_choice()
		dest_choice(destination)

def jungle():
	print "Seeing the think lush jungle at the end of the beach brings butterflies into %s's stomach. Blaming it on bad wind from last night's dinner he prepares himself for the journey." % name
	equip()

def mountain():
	print "The mountain looms forth as %s tilts his head back to get a better look. A wisp of cloud encircles the summit which rises to a sharp point. %s starts to plan in his mind what he'll need for the ascent." % (name, name)
	equip()

def swamp():
	print "The smell eminating from the bog could be appreciated even from this far away, it looked gloomy and dark. %s wondered what kind of creatures lay in wait amongst the reeds, he also wondered if they would be hungry. %s checked his bag for what he would need." % (name, name)
	equip()

def equip():
	print "Reaching into the bag %s found 4 items to choose from, which would be most suitable for the " % name + destination + "?"
	print """%s has to choose between:\n
		\t* machete\n
		\t* rope\n
		\t* dingy\n""" % name
	global equip_choice
	equip_choice = raw_input("What does %s choose? " % name)
	if equip_choice == "machete":
		if destination == "jungle":
			print "%s hacks his way through the jungle with the %s in glorious triumph slaying all the wild beasts before %s, he takes the head of a four headed leaopard as his prize and returns to the shore to wait to be picked up!" % (name, equip_choice, sex)
		elif destination == "mountain":
			print "As %s began to climb the mountain the realisation quickly washed him that the %s was of no use here, while trying to put it back in his bag he slipped and smashed his soul against the rocks below."
		elif destination == "swamp":
			print "The %s allowed %s to cut through the reeds with ease, but as he wass up to %s waist in sludgy swamp water he doesn't notice the crocopotimus eating him whole from behind." % (equip_choice, name, sex)
		else:
			print "That wasn't in the bag, %s picks again." % name
			equip()
	elif equip_choice == "rope":
		if destination == "jungle":
			print "Mistaking the %s for a snake %s panics and runs up the nearest tree, it is here that he is squeezed into jelly and eaten by a snake." % (equip_choice, name)
		elif destination == "mountain":
			print "With nothing more than the %s, %s scales the lofty heights of the %s and stabs a flag into its summit with great force and pride!" % (equip_choice, name, destination)
		elif destination == "swamp":
			print "%s gets horribly tangled in the %s and dies from a combination of stranglation and drowning." % (name, destination)
		else:
			print "That wasn't in the bag, %s picks again." % name
			equip()
	elif equip_choice == "dingy":
		if destination == "swamp":
			print "Full of vigor and sass %s ploughs bow first through the entrails of the %s in the %s discovering a variety of native fauna he is very pleased with." % (name, destination, equip_choice)
		elif destination == "jungle":
			print "While trying to blow up the %s %s passes out from exhaustion and wakes up dead in the belly of a rhinosotops. The %s is no place for idiocy" % (equip_choice, name, destination)
		elif destination == "mountain":
			print "A quarter of the way up the %s the wind picks up and gets a hold of the %s, it pulls it and %s off the %s plunging them to their doom. The %s survives and realses a best selling novel on the expedition." % (destination, equip_choice, name, destination, equip_choice)
		else:
			print "That wasn't in the bag, %s picks again." % name
			equip()
	else:
		print "That wasn't in the bag!, %s picks again." % name
		equip()
			
print """An adventurer of mild manner and poor judgement lands on the shores of the newly discovered island of Whitestone. It is an ominous place, bringing forth a sense of foreboding.
Our adventurer is here to chart the island of its landscape and fauna, the general consensus is still undecided if he is brave or stupid.\n"""

name = raw_input("What was his name again? ")

print "A of course, how could I forget. %s is such a strong name. " % name

sex = raw_input("Is that a his or her name? ")

print "My apologies, in this day and age names such as %s don't always mean it's a %s name!" % (name, sex)

print "After landing on the beach " + name + " waves goodbye to the ship he disembarked from, it set sail as soon as he had gotten off - they did not want to hang around.\n"

def first_choice():
	print "He scanned his horizon and saw 3 options;\n\t* jungle\n\t* mountain\n\t* swamp\n" + name + " thinks about it breifly but then decides "
	global destination
	destination = raw_input(" ")

first_choice()

dest_choice(destination)

print "And so conludes the adventure of %s." % name
