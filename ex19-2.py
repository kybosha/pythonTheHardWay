from sys import argv

script, team1 = argv

my_team = 'Liverpool'

def ten_way_funct(your_team):
	print "Ah so you support %r" % your_team

real_team = raw_input("What's your team again? ")

def my_funct(real_team):
	if real_team == "Man U":
		return "Man U"
	else:
		return "No other team exists!"


# add in the argv
ten_way_funct(team1)

ten_way_funct('Chelsea')
ten_way_funct(raw_input("What's your team? "))
ten_way_funct(my_team)
# pass in the returned value of 'my_funct' to the original function
ten_way_funct(my_funct(real_team))


