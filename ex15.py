# import sys module
from sys import argv

# get arguments
script, filename = argv

# set txt var consisting of file object
txt = open(filename)

# indicate which file is being output
print "Here's your file %r:" % filename

# output the contents of the file
print txt.read()
txt.close()

# ask user to enter the filename again and store it in a var
print "Type the filename again:"
file_again = raw_input("> ")

# set another var consisting of the file object
txt_again = open(file_again)

# output the contents again
print txt_again.read()
txt_again.close()
