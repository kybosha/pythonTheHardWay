print "You enter a dark room with two doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck, Good job!"

elif door == "3":
	print "A hungry giant looms over you, thirsty for violence.\n"
	print "It turns out though there are 3 Gods listening right now.\n"
	print "Which one do you wish to beg for divine intervention?\n"
	print "1. Annubis."
	print "2. John Frum."
	print "3. Jesus's cousin Gary."
	print "Pick another deity."
	
	prayer = raw_input("> ")

	if prayer == "1":
		print "The Giant is instantly mummified and you dance around his corpse before making a house from his sizeable carcass."
	elif prayer == "2":
		print "John Frum appears and defeats the bear in single handed combat."
	elif prayer == "3":
		print "Gary appears and tries to calm the Giant with Chritian nonesene, he is devoured immediately. Gary was a big guy so now the Giant is full, he gives you permisison to leave."
	else:
		print "We wold you there was noone else listening, you are butchered by the giant who ensures you stay alive long enough to regret your decision."

else:
	print "You stumble around and fall on a knife and die. Good job!"
	
