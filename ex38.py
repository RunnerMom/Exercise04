# exercise 38 LPTHW
# Day 4 at Hackbright


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there aren't 10 things in that list, let's fix that"

#create a list that takes ten_things and delimits by space
stuff = ten_things.split(' ')

#create a list with more things to add to ten things
more_stuff = ["day", "night", "song", "grisbee", "Corn", "banana", "girl", "boy"]

#append stuff list until you get to ten things

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are now %d items" % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

