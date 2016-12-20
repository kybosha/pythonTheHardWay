# House of Horrors Python Game - ai of the game is to escape the house of horros alive, the only method of escape is by driving away in the car parked out front whose keys you need to find. 
# Follow the instructions and make your descions wisely.
import random

print "Let's start with a few questions."

shower_leak = False

items = []
# get the user's name
def your_name():
	global name
	print "What's your name?"
	name = raw_input("> ")
	return name

#BMI calculation

def divide(a, b):
        return a / b

def bmi_capture():
	global weight
	global height
	weight = float(raw_input("What is your weight in Kilograms: "))
	height = float(raw_input("What is your height in Metres: "))
	return weight, height

def calculate_bmi(c, d):
        bmi = float(divide(divide(weight, height), height))
        return bmi

your_name()
bmi_capture()

bmi = calculate_bmi(weight, height)

def r_u_fat(e):
        if 18.5 > e:
                return "Underweight"
        elif 24.9 > e > 18.5:
                return "Normal Weight"
        elif 29.9 <= e:
                return "Overweight"
        else:
                return "Obese"

state = r_u_fat(bmi)

#print bmi, state + "\n"

#END OF BMI CALC


# The opening sequence
def start():
	print """A test, a test for the soul while the mind is occupied. Save your soul and your mind may just flicker again, consciousness is a cruel concept. You need a foundation, 
	a corner stone in which to base your percpetions on, don't keep your eyeys shut for too long, when you open them things may seem too real. I understand, you're confused. That's 
	perfectly reasonable, but you you need to take action now if you wish to become lucid again. Now wake up, but not completely, you can only save yourself if your self thinks it's awake.
	\nI can be of some assistance later on, things may become clearer, but for now wake up!\n"""

	print "Wake up!\n" * 5
	
	wake()

def wake():
	print """As his eyes creaked opened he became aware of the throbbing pain that was present in the back of his head. Reaching back he brushed his fingers across an an egg sized 
	lump that plateaued out from his head, it felt as though it was buffering against his brain as the vibrations could be felt throughout his body. As his surroundings started to 
	become clear he realised he was lying on his side surrounded by a quilt of fallen autumn leaves, as he shifted his weight they crunched underneath him clunging to his clothes 
	while he pushed himself up. Craning his neck he could see he was surrounded by woodland, it was extremely dark though 
	so he could only see the first row of trees. The only light source available was the dull glow of the moon, it excentuated the silhouettes of the objects that surrounded him but 
	didn't reveal any more detail. There was a break in the trees far off to his right and stationed in front of it was a small car, he couldn't make out much more than that due to 
	the low visibility.\n Suddenly there was a bang behind him, he jolted round he found himself outside the front of an old wooden house, it was a 2 storey cabin. Agahst he scanned 
	the front of the house erratically searching for the source of the noise. All was quiet though. Too quiet he thought, there were no animal noises, no trees rustling in the wind. 
	In fact there was no wind at all. The back of his head began to throb again causing him to double over as he clutched at the swollen lump pertruding from it. ****WRITE MORE***
	"""
	print "Panic rose up from his gut filling his mind with anxiety, he had a split decision to make, run or enter the house?"
	enter_run = raw_input("> ")
	if "run" in enter_run:
		run()
	else:
		enter_house()




def run():
	print """Run out towards the car - reach car - realise it is locked - keys must be in house - decision around whether to go into the house to look for them or make for the clearing in the 
	woods.\n
	"""
	woods_house = raw_input("> ")
	if "house" in woods_house:
		enter_house()
	elif "woods" in woods_house:
		trap()
	else:
		print "There were only 2 options for him at this point"
		run()

def enter_house():
	print """House is entered looks around a bit blah blah blah, on the floor he finds a note written on a post-it note. Not sure where the basement is just yet.  
	Note reads that the car keys have been left in the safe in the basement, combination is 17XX - the last 2 digits are unintellgible.\n \"I need to find those last 2 digits he thought.\""""
	downstairs_upstairs()

def stairs():
	print """stairs
	"""

def basement():
	print """basement
	"""

def riddle_me_this():
	print """
	"""

def trap():
	print "Running towards gap, falls into hidden trap in floor breaking leg, decision - cry for help, sleep and wait for morning" 
	sleep_cry = raw_input("> ")
	if "sleep" in sleep_cry or "morning" in sleep_cry:
		wake()
	elif "cry" in sleep_cry or "help" in sleep_cry:
		print "Noise alerts dark figure, dark figure shoots him dead."
		dead("Face becomes a bum")
	else:
		print "Only options available are those 2"
		trap()

def dead(reason):
	print reason, ",guy wakes up. Shit gets real."

def downstairs_upstairs():
	print "Does he go upstairs or stay on the ground floor"
	down_up = raw_input("> ")
	if "upstairs" in down_up:
		up()
	elif "down" in down_up:
		downstairs()
	else:
		print "Only options available are those 2"
		downstairs_upstairs()

def up():
	print """He walks up stairs and finds a long straight corridor with 3 rooms, 2 on the left 1 on the right. blah blah blah - does he enter one or head back downstairs?"""
	upstairs_room_choice = raw_input("> ")
	if "1" in upstairs_room_choice:
		print "Blah Blah blah - He enters the first room"
		room1()
	elif "2" in upstairs_room_choice:
		print "Blah Blah blah - He enters the second room"
		room2()
	elif "3" in upstairs_room_choice:
		print "Blah Blah blah - He enters the third room"
		room3()
	elif "down" in upstairs_room_choice:
		downstairs()


def room1():
	print """Enters room 1 - turns out to be a bedroom, bedframe with bedside table, wardrobe. What should he inspect?
	"""
	room1_inspect = raw_input("> ")
	if "bed" in room1_inspect:
		print "Shit about what the bed looks like\n"
		print "should he check the wardrobe as well or go back to the landing?"
		room1_inspect2 = raw_input("> ")
		if "wardrobe" in room1_inspect2:
			print "Nothing but coat hangers in the wardrobe, pick it up?"
			wardrobe_choice = raw_input("> ")
			if "pick" in wardrobe_choice:
				while "Coat Hanger" in items:
					print "You already have the Coat Hanger."
					return room1()
				print "Coat hanger is picked up"
				items.append("Coat Hanger")
				print "Heads back out to the landing."
				print items
				upstairs_hallway()
				
			else:
				print "Didn't pick up the coat hanger and heads back out to the landing"
				upstairs_hallway()
		elif "landing" in room1_inspect2:
			upstairs_hallway()
		else:
			return room1()
	elif "wardrobe" in room1_inspect:
		print "Nothing but coat hangers in the wardrobe, pick it up?"
		wardrobe_choice = raw_input("> ")
		if "pick" in wardrobe_choice:
			while "Coat Hanger" in items:
					print "You already have the Coat Hanger."
					return room1()
			print "Coat hanger is picked up"
			items.append("Coat Hanger")
			print "Leaves the room back to landing"
			upstairs_hallway()
		else:
			print "Didn't pick up the coat hanger and heads back out to the landing"
			upstairs_hallway()
	elif "landing" in room1_inspect:
		print "Leaves the room back to landing"
		upstairs_hallway()
	else:
		print "No option like that"
		return room1()
		

	
def room2():
	print """Enters room 2 - it's the bathroom, blah blah blah. There's a shower, a broken toilet bowl and not much else. The light is flickering, the shower is dripping heavily
	turn the shower handle to stop the dripping? 
"""	
	
	shower_turn = raw_input("> ")
	if "turn" in shower_turn:
		while "Coat Hanger" in items:
			print "...turns the handle, all hell breaks lose. Water gushing everywhere, uses the Coat Hanger to fix the leak. back to the landing."
			items.remove('Coat Hanger')
# REMOVE AFTER TESTING
			print items
			global shower_leak
			shower_leak = True
			# REMOVE after teting
			print shower_leak
			upstairs_hallway()
# REMOVE AFTER TESTING
		print items
		print " There was no way to fix this so he gets the hell out of there!"
		
		upstairs_hallway()

	else:
		print "The dripping wasn't so bad after all blah blah blah, back to the landing"
		shower_leak is False
# REMOVE AFTER TESTING
		print items
		upstairs_hallway()


def room3():
	print """ Third room is a study/office, it is baren except for a desk in front of a large bare window looking out onto the front yard of the house, 
	the only light entering the room dully creeps in from the distant moon - blah blah blah. Walking over to the desk what should be explored? 
	Look out the window, check out desk?

	"""
	window_desk = raw_input("> ")
	if "window" in window_desk:
		print """He looks out the window out across the yard...blah blah blah, he can see the outline of the car out towards the tree line reminding him
		of what his goals are. He needs to get into that basement, where's the key though? And what's the rest of the combination for the safe? Should he check out
		the desk now or head back out the room?"""
		desk_leave = raw_input("> ")
		if "leave" in desk_leave:
			print "Heads back out to the landing."
			upstairs_hallway()
		elif "desk" in desk_leave:
			print """Turning his gaze away from the window he looks over the desk, pretty dark so he's not able to see much, tries to open the drawers he finds
			but they are empty. There's an old lamp sitting on the top of the desk, it may still work should he turn it on?"""
			room3_lamp()
		else:
			print "That's not an option."
			room3()
	elif "desk" in window_desk:
		print "Shit about the desk, ask whether to look out the window or leave."
		window_leave = raw_input("> ")
		if "window" in window_leave:
			print "He looks out the window out across the yard...blah blah blah then turns and leaves the room."
			upstairs_hallway()
		else:
			print """He leaves the room, but hears a rustling from the corner of the room making he swing round in fright. There's nothing there so he leaves again, he then 
			hears a whisper \"LAMP\""""
			upstairs_hallway()


def room3_lamp():
	lamp_decision = raw_input("> ")
	if "on" in lamp_decision:
		lamp_on = True
	else:
		lamp_on = False

	if lamp_on is True:
		print """He turns on the lamp, it fizzes and flickers as it attmepts to illuminate the desk, after a few seconds of flickering it goes full beam blinding him, he shields
		his eyes momentarily. Slowly his eyes begin to adjust to the new lighting level and drops his arm from his eyes, he's looking at the window now but the new ligting means
		it's reflected and so it is himself and the room that is looking back at him. He notices a post-it notepad in the refelction of the window resting on the table now. Picking it up 
		he can see there are imprints on it...it must be the pad that the note he found was written on. Holding it under the lamp he can see it clearly, scanning it quickly he finds the the full
		code - 1792!"""
		code = 1792
		items.append(code)
		print items
		print "Back to the landing."
		upstairs_hallway()
		

	else:
		print "Turns and leaves the room."
#add in a function to display when on the landing with the option to go back downstairs!!!
		upstairs_hallway()
 
def upstairs_hallway():
 	print """He found himself back in the upstairs hallway, glancing around he could see the 3 rooms again. Should he go downstairs or enter one of the 3 rooms?

 	"""
	upstairs_hallway_choice = raw_input("> ")
	if "down" in upstairs_hallway_choice:
		print "He heads back down the stairs blah blah blah"
		downstairs()
	elif "1" in upstairs_hallway_choice:
		room1()
	elif "2" in upstairs_hallway_choice:
		room2()
	elif "3" in upstairs_hallway_choice:
		room3()
	else:
		print "That aint not choice"
		upstairs_hallway()

def downstairs():
	print """On the ground floor he blah blah blah blah - looks around a little there are 4 rooms, more description about what he sees, he needs to pick a room - A, 
	B, C, or D Or should he go upstairs?"""
	downstairs_room_choice = raw_input("> ")
	if "a" in downstairs_room_choice:
		print "He enters room A"
		rooma()
	elif "b" in downstairs_room_choice:
		print "He enters room B"
		roomb()
	elif "c" in downstairs_room_choice:
		print "He enters room C"
		roomc()
	elif "d" in downstairs_room_choice:
		print "He approaches room D"
		roomd()
	elif "up" in downstairs_room_choice:
		upstairs_hallway()
	else:
		print "Crackerjack that aint no choice!"
		downstairs()




def rooma():
	print """Enters Room A blah blah blah - it's the kitchen, looks around blah blah blah blah. Description of the kitchen and it's rustic demeanor. Get to the point 
	where something enters and he has to reach for a knife but drops it down a crack and tries to reach for it in order to defend himself. The crack is slim, """
	if state == "Overweight" or state == "Obese":
		print "You too fat! You dead! blah blah blah monster rips you to pieces"
		dead("Monster tears you a new one.")
	else:
		print "you manage to pull the knife out and begin the epic battle with the demon\n He's terrifying!"
		print """
		                    ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'


		"""
		battle()

def battle():
	while "Knife" in items:
					print "The body of the demon lies in its own filth. You head back out to the landing."
					return downstairs()
	print "The demon lunges at you, lunging forward with the knife you aim for it's chest"
	your_num = random.randrange(1, 10)
	# for testing purposes
	print "your num is %d" % your_num
	beast_num = random.randrange(1, 10)
	# for testing purposess
	print "beasts num is %d" % beast_num
	if beast_num > your_num:
		print "He knocks you back and comes in again for the kill, you bring up the knife again to protect yourself."
		your_num2 = random.randrange(1, 10)
		# for testing purposes
		print "your num2 is %d" % your_num2
		beast_num2 = random.randrange(1, 10)
		# for testing purposes
		print "beasts num2 is %d" % beast_num2
		if beast_num2 > your_num2:
			dead("Knocks knife out of hand and fucks you up")
		elif beast_num2 == your_num2:
			if state == "Normal Weight":
				print "EPIC FIGHT SCENE resulting in your victory. You pocket the knife and move back out to the hallway"
				items.append("Knife")
				downstairs()
			else:
				dead("EPIC BATTLE WITH YOUR DEMISE")
		else:
			print "you rip that demon a new one and drink his blood in a crazed victory ceremony and go back out to the downstairs hallway."
			downstairs()
	else:
		print "QUICK DEATH FOR THE BEAST you go back out to the hallway."
		items.append("Knife")
		downstairs()

def roomb():
	print "The room is empty, nothing to see here, back out to the hallway."
	downstairs()

	
def roomc():
	print shower_leak
	if shower_leak is True:
		print """You enter into the room in the far right corner of the downstairs area, it appears to be an old library....blah blah blah,
		browse the books, they have no writing in them? Strange and pondering thoughts ensue. blah blah blah blah. \n

		You step in a patch of water alerting you to a dripping noise. You look up to see a large damp patch bluging from the ceiling, you must be under the bathroom!
		The shower leak coupled with the old flooring! \n 
		The ceiling comes crashing down on top of you crushing your very existence.
		"""
		dead("You are turned to jelly by the weight of the rubble.")
	else:
		print """ You scour the library for literary delights blah blah blah blah blah blah then return to the hallway."""
		downstairs()



	""" INVESTIGATE!!!! Strange transition to dead if shower_leak is True - 


"""

	
"""

	def car():
"""	


start()


