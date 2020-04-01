# Cian Hogan
# create a function that estimates the square root, cont.. 
# of a positive input, print the approx square root to two decimal places
# Newtons Formula link https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

# define the function for estimating square root
def sqroot(x):
	x = float(x)
	count = 1.0 # set an iterator variable
	# loop to find closest square number to input x
	# keep adding 1 to count until count squared is bigger than x
	while True:
	# if count squared = x break the loop
		if count * count == x:
			root = count
			break # from while true loop
	# if count squared less than x increase x by 1
		elif count * count < x:
			count = count + 1
	# When count squared is greater than x estimate square root
		elif count * count > x:
			root = count
			# newtons formula for square root
			while round(root*root, 2) != x:
				root = (1/2) * (root + (x/root))			
			break # break from trie loop when root**2 = input value X
	# return square root
	return root

# Get input from the user, convert to float
try:
	i = float(input("Please enter a positive number: "))

	# use new function on input
	iroot = sqroot(i)
	# print result of funtion, rounded to 2 decimals
	print("The square root of", i, "is approx.", round(iroot, 2))

# Print an error message if the user entered an incorrect value 
except ValueError:
	print("Are you sure you entered a positive number? Try again")
