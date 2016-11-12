from sys import argv

# add in argument variables
script, input_file = argv

# fucntion to print the whole content of the file
def print_all(f):
	print f.read()

# funciton to move the "pointer" back to the beginning of the file
def rewind(f):
	print f.read()

# move the pointer back to the first byte
def rewind(f):
	f.seek(0)
# 
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open the passed in file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print all the contents of the file as well as it's line number
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind the file
rewind(current_file)

print "Let's print three lines:"

# current_line is equal to the first line in the file
current_line = 1
print_a_line(current_line, current_file)

# current_file is equal to the second line
current_line += current_line
print_a_line(current_line, current_file)

# current_line is equal to the third line
current_line = current_line + 1
print_a_line(current_line, current_file)
