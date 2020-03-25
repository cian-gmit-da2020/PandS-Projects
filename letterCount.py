# Cian Hogan Week 7 task
# Count how many letter e's are in the file mobydick.txt
# easter egg third argument to check any single character
# import sys module
import sys

# make sure user has entered enough arguments
try:
	fname = str(sys.argv[1]) # convert second command line argument to string

	# set default check for letter e
	letter = "e"

	# if user enters a third argument search for that letter instead
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

# print out error if user doesnt enter a filename argument
except IndexError:
	print("Looks like you didn't enter a filename.")
	print("Try 'python letterCount.py your_filename_here' ")

# print out error if user doesnt enter a valid filename
except FileNotFoundError:
	print("Are you sure that %s is a valid filename?" % (fname))
	print("Double check and try again")