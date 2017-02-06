import collections

list1 = ["Hand", "Foot", "Fingers", "Thumbs", "Toes"]

list2 = {}

list2['Barry'] = {}

list2['Barry']['Age'] = 23
list2['Barry']['Sex'] = str("M")
list2['Barry']['Nationality'] = str("English")

list2['Roo'] = {}
list2['Roo']['Age'] = 21
list2['Roo']['Sex'] = str("F")
list2['Roo']['Nationality'] = str("Spanish")

print list1, list2

print list1.pop()

for key, value in list2.iteritems():
	print (key, value)
