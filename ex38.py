ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# split(ten_things, ' ')
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # create a var containing the last item in the more_stuff list and removes that item from the more_stuff list
    next_one = more_stuff.pop()
    print "Adding: ", next_one

    # append(stuff, next_one)
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy

# pop(stuff)
print stuff.pop()

# join(stuff, ' ')
print ' '.join(stuff) # what? cool!

# @todo it seems like the following should output Telephone#Sugar but it outputs Telephone#Light
#       find out why.
#      - Telephone is fourth item in list (index of 3)
#      - Light is fifth item in list (index of 4)
#      - Sugar is sixth item in list (index of 5)

# join(stuff[3:5], "#")
print '#'.join(stuff[3:5]) # super stellar!
