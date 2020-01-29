# Cian Hogan
# Take an input string and output every second letter in reverse order

# Takes input from user
string = input("Enter a sentence here: ")

# reverses the input
revstring = string[len(string)::-1]

# creates empty list
secondletters = []

# loops through each letter in the reversed string
for i in range(0, len(revstring)):

	# checks if the letter is a space character and adds spaces to list
	if revstring[i] == " ":
		secondletters.append(revstring[i])

	# checks for even indexes and adds to list
	elif i % 2 == 0:
		secondletters.append(revstring[i])
		
	# Skips odd indexes
	else:
		continue

# joins the list together into new string and prints
print("".join(secondletters))

