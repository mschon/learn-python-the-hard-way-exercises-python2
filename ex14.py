from sys import argv
script, user_name, location = argv
prompt = '$ '

print "Hi %s of %s, I'm the %s script." % (user_name, location, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you work %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You work in %r. Not sure what that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
