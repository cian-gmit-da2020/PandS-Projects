# Cian Hogan Week 7 task
# import sys module
import sys

# convert final command line argument to string
fname = str(sys.argv[1]) 
# set default check for letter e
letter = "e"

# if user enters an extra argument search for that letter instead
if len(sys.argv) == 3:
	# check the extra argument is a single character
	if len(sys.argv[2]) == 1:
		letter = str(sys.argv[2])

# open file in read mode
with open(fname, 'r') as f:
	count = 0
	for line in f:
	# iterate through each character in the line
		for char in line:
	# if the char is a match increment count by 1
			if char == letter:
				count += 1


# print results of script
print("There are %d letter %s's in %s." % (count, letter, fname))

