# Cian Hogan Week 7 task
# import sys module

import sys

# convert final command line argument to string
fname = str(sys.argv[-1])

# open file in read mode
f = open(fname, 'r')

# convert the file to a list of lines
lines = f.readlines()
# set iterator to 0
count = 0
# for line in the list lines check each letter
for line in lines:
	# for each character in the line string check if it is 'e'
	for char in line:
	# if its e increment count by 1
		if char == "e": # or char == "E":
			count += 1

# close file f
f.close()

# print results of script
print("There are", count, "e's in", fname)
