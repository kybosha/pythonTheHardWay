# House of Horrors Python Game - aim of the game is to escape the house of horros alive, the only method of escape is by driving away in the car parked out front whose keys you need to find. 
# Follow the instructions and make your descions wisely.
import random
import os,sys
import text
import time
from random import randrange

print opening_line
#print "Let's start with a few questions."

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

# Safe code

code = 1729

def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')

# The opening sequence
def start():
	print "THIS IS A TEST!!!"
	"""for i in start_text.split():
		sys.stdout.write("{} ".format(i))
		sys.stdout.flush()

		seconds = ".6" + str(randrange(1,5,2))
		seconds = float(seconds)
		time.sleep(seconds)"""

	print start_text.split()

	print "Wake up!\n" * 5
	
	wake()

def wake():
	print wake_text
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
	print enter_house_text
	downstairs_upstairs()


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
	print upstairs_text
	upstairs_room_choice = raw_input("> ")
	if "1" in upstairs_room_choice:
		print room1_entry_text
		room1()
	elif "2" in upstairs_room_choice:
		print room2_entry_text
		room2()
	elif "3" in upstairs_room_choice:
		print room3_entry_text
		room3()
	elif "down" in upstairs_room_choice:
		downstairs()


def room1():
	print room1_initial_text
	room1_inspect = raw_input("> ")
	if "bed" in room1_inspect:
		print room1_bed_text
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
	print room2_initial_text
	shower_turn = raw_input("> ")
	if "turn" in shower_turn:
		if "Coat Hanger" in items:
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
		else:
			print items
			print " There was no way to fix this so he gets the hell out of there!"
		
			upstairs_hallway()

	else:
		print room2_no_fix_shower
		shower_leak is False
# REMOVE AFTER TESTING
		print items
		upstairs_hallway()


def room3():
	print room3_initial_text
	window_desk = raw_input("> ")
	if "window" in window_desk:
		print room3_window_text
		desk_leave = raw_input("> ")
		if "leave" in desk_leave:
			print "Heads back out to the landing."
			upstairs_hallway()
		elif "desk" in desk_leave:
			print room3_window_desk_text
			room3_lamp()
		else:
			print "That's not an option."
			room3()
	elif "desk" in window_desk:
		print room3_desk_text
		window_leave = raw_input("> ")
		if "window" in window_leave:
			print room3_desk_window_text
			upstairs_hallway()
		else:
			print room3_whisper_text
			upstairs_hallway()


def room3_lamp():
	lamp_decision = raw_input("> ")
	if "on" in lamp_decision:
		lamp_on = True
	else:
		lamp_on = False

	if lamp_on is True:
		print room3_lamp_text
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
		print upstairs_hallway_choice_down
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
	print downstairs_initial_text
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
	elif "out" in downstairs_room_choice:
		return back_outside()
	else:
		print "Crackerjack that aint no choice!"
		downstairs()




def rooma():
	while "Knife" in items:
					print "The body of the demon lies in its own filth. You head back out to the landing."
					return downstairs()
	print rooma_intial_text
	if state == "Overweight" or state == "Obese":
		print rooma_too_fat_text
		dead("Monster tears you a new one.")
	else:
		print "you manage to pull the knife out and begin the epic battle with the demon\n He's terrifying!"
		print demon_text
		battle()

def battle():
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


def roomd():
	print """Approaches 'roomd' blah blah blah - it's the basement! You try the door handle, it's locked. There is a grate at the base of the door and you notice 
	something glistening in it. It's a set of keys."""
	if "Coat Hanger" in items:
		print """You remember you have the coat hanger and bending it out you turn it into a hook and pull the keys up out of the grate. Then you open the basement door
		and make your desent."""
		items.append("Basement Keys")
		global basement_door_unlocked
		basement_door_unlocked = True
		basement()
	else:
		print "You can't reach the keys, you need to go and find something that can help you get them out. You turn back to the downstairs hall. \n The strange voice returns urging you to go back upstairs."
		downstairs()


def basement():
	print """Basement scene - blah blah blah, you see the safe in a corner, do you go straight to it or explore the basement futher?"""
	basement_choice = raw_input("> ")
	if "explore" in basement_choice:
		explore_basement()
	elif "safe" in basement_choice:
		print "You approach the safe, reaching it you dust off the dial and remember a code needs to be entered."
		if code in items:
			print "You have the code! Pull out piece of paper, code is %d" % code
			the_safe()
		else:
			print "You never found the last 2 digits, I guess you could take a guess? Or go back and look for the other digits?"
			guess_or_look = raw_input("> ")
			if "guess" in guess_or_look:
				the_safe()
			else:
				print "you head back to the first floor to look for the rest of the code.\n The strange voice returns urging you to go back upstairs."
				downstairs()

def explore_basement():
	print """Wondering around the basement blah blah blah, you knock over a pile of boxes - a creepy old man emerges from the shadows. You shite yourslef, or atleast it feels like you did. The old man grins a
	torid smile and then tells you he has a riddle for you. If you answer correctly he will gift you something, if you answer incorrectly something terrible will happen. One word is requied for te answer.\n"""
	
	print poem
	print "With a death like expression he demands an answer."
	riddle_answer = raw_input("> ")
	if "inferno" in riddle_answer:
		print "The old man's smile thins and with a reluctant nod he congratulates you on your correct answer. blah blah blah he allows you to continue on your way and head back to the safe."
		return the_safe()
	else:
		print "The old man's smile broadens and he lets out an evil cackle, 'times up he screams!'\n"	

		print skull
		dead("The old man sucks out your very soul.")



def the_safe():
	print "You approach the safe and notice it's a dial safe, you start to enter the code."
	if code in items:
		print "You have the code, it's %d. Enter it in." % code
		code_input = raw_input("> ")
		if code_input == 1729:
			print "The safe clicks open, you've got the keys! You rush out of the basement back up to the downstairs area."
			items.append('keys')
			downstairs()
		else:
			return wrong_code()
	else:
		print "you enter 1 and 7, but guess the last 2 digits."
		code_guess = raw_input("> ")
		if '29' in code_guess:
			print "The safe clicks open, you've got the keys! You rush out of the basement back up to the downstairs area."
			items.append('Car Keys')
			downstairs()
		else:
			print "The safe explodes and you are blown to pieces."
			return dead("Your body parts scatter the basement floor.")

	

def back_outside():
	if 'Car Keys' in items:
		print "You have the car keys, let's go to the car and get out of here!"
		return car()
	else:
		print "You hear that voice again - you need the car keys, second floor!\n"
		print "Will you go back into the house or continue to the car?"
		outside_decision = raw_input("> ")
		if "house" in outside_decision:
			return downstairs()
		elif "car" in outside_decision:
			return run()
		else:
			print "That aint not choice"
			back_outside()

def car():
	print "Reaching the car and open it up with the keys. Start the engine and get drive out through the gap in the trees.\n"
	print car_text2


start()


