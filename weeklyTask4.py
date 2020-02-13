# Cian Hogan week 4 task
# take input and in its even divide by 2 if its odd muliply by 3 and add one

# make sure the program doesnt crash if user enters an invalid response
try:
	num = int(input("Enter a positive whole number: "))
# make sure the user enters a positive number
	if num > 0:
		while num != 1: # run until num is 1

			if num % 2 == 0: # check for even number
				num = num/2
				print(int(num))

			else:
				num = (num * 3) + 1
				print(int(num))

	else: # print out for input of negative number	
		print(num, "Doesn't look like a positive whole number ")

except: # print out for user input error
	print("Are you sure you entered a whole number? Try again")