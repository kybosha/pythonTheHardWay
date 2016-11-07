#Import required modules
from sys import argv

#Pass in the vars
script, filename = argv

# Add the contents of the passed in file to the txt variable
txt = open(filename)

#print out the contents of the txt variable which contains the passed in file's contents
print "Here's your file %r:" % filename
print txt.read()

# Take in the filename again
print "Type the filename again:"
file_again = raw_input("> ")

# Add the contents of the passed in file to the txt_again variable 
txt_again = open(file_again)

# print the contents out
print txt_again.read()

# close the files out
txt.close()
txt_again.close()
