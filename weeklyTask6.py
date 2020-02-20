# Cian Hogan
# create a function that estimates the square root, cont.. 
# of a positive input, rough estimate using division

# define the function
def sqroot(x):
	count = 1 # set a iterator variable
	# loop to find closest square number to input x
	# keep adding 1 to count until count squared is bigger than x
	while True: 
		if count * count < x:
			count = count + 1
	# When count squared is greater than x jump out of loop
		elif count * count > x:
			break
	# find x diveded by the squares closest but greater and less than x
	low = x / (count - 1)
	high = x / (count)
	# find the avegrage of above as estimate square root
	root = (low + high) / 2
	# return square root
	return root

# Get input from the user, convert to float
i = float(input("Please enter a positive number: "))

# use new function on input
iroot = sqroot(i)

# print result of funtion, rounded to 2 decimals
print("The square root of", i, "is approx.", round(iroot, 1))

