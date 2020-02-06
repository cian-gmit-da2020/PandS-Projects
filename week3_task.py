# Cian Hogan week 3 task
# Take an input string and outputs every second letter in reverse order

# Takes input from user
string = input("Enter a sentence here: ")

# reverses the input
revstring = string[len(string)::-1]

# prints every second char of revstring
print(revstring[0::2])

