# define a function that executes a while loop and prints output
def run_the_numbers_while(limit, increment):
    i = 0
    numbers = []
    print "output for \"while\" loop version of function:"
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

# @todo write a run_the_numbers_for function similar to the above, but using a
#       for loop instead of while loop.

# use while loop to count up to (not including) 6, incrementing by 1
run_the_numbers_while(6, 1)

# @todo call the run_the_numbers_for function
