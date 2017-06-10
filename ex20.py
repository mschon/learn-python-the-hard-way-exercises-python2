from sys import argv

script, input_file = argv

# define functions

# define a function to output the entire file contents
def print_all(f):
    print f.read()

# define a function to return position to beginning of file
def rewind(f):
    f.seek(0)

# define a function to output line number and line contents
def print_a_line(line_count, f):
    print line_count, f.readline()

# create a var containing file object
current_file = open(input_file)

# call func to print entire file contents
print "First let's print the whole file:\n"
print_all(current_file)

# call func to move position to beginning of file
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

# set the current_line to 1 and print the ln and call the func to print a ln
current_line = 1
print_a_line(current_line, current_file)

# increment current_line by 1 (to ln 2) and call the func to print a ln
current_line += 1
print_a_line(current_line, current_file)

# increment current_line by 1 (to ln 3) and call the func to print a ln
current_line += 1
print_a_line(current_line, current_file)
