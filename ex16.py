from sys import argv

script, filename = argv

newline = "\n"

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# don't really need to truncate() because opening in w mode truncates it already
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# set a var containing what we want to write
contents = "%s%s%s%s%s%s" % (line1, newline, line2, newline, line3, newline)

# write to the file
target.write(contents)

print "Now we close it."
target.close()

print "I'm going to print out the contents of the file."

txt = open(filename)
print txt.read()

print "And finally, we close it again."
txt.close()
