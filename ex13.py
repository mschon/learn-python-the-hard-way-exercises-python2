# import the sys module
from sys import argv

script, first, second, third = argv

custom = raw_input("Give me some text")

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
print "You said: ", custom
