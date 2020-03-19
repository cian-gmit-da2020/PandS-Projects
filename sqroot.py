# Cian Hogan
# create a function that estimates the square root, cont.. 
# of a positive input, rough estimate using division
# Newtons Formula link https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

# define the function
def sqroot(x):
	x = float(x)
	count = 1.0 # set a iterator variable
	# loop to find closest square number to input x
	# keep adding 1 to count until count squared is bigger than x
	while True:
	# if count squared = x break the loop
		if count * count == x:
			root = count
			break
	# if count squared less than x increase x by 1
		elif count * count < x:
			count = count + 1
	# When count squared is greater than x estimate square root
		elif count * count > x:
	# find x divided by the squares closest but greater and less than x
			low = x / (count - 1)
			high = x / (count)
	# find the avegrage of above as estimate square root
			root = (low + high) / 2
			# newtons formula for square root
			while round(root*root, 2) != x:
				root = (1/2) * (root + (x/root))
				
			break
	# return square root
	return root

# Get input from the user, convert to float
try:
	i = float(input("Please enter a positive number: "))

	# use new function on input
	iroot = sqroot(i)

	# print result of funtion, rounded to 2 decimals
	print("The square root of", i, "is approx.", round(iroot, 1))

# Print an error message if the user entered an incorrect value 
except ValueError:
	print("Are you sure you entered a positive number? Try again")
