# Cian Hogan week 2 task
# BMI = Weight(KG)/(Height(m)**2
# https://en.wikipedia.org/wiki/Body_mass_index

# Get input from user, checking that the input type is correct
try:
	weight = float(input("What is your weight in Kilograms(KG): "))
	height = float(input("What is your height in Meters(M): "))

	# work out bmi score
	bmi = weight/(height**2)

	# Print out different result depending on bmi score
	if bmi < 18.5:
		print("You have a BMI of ", round(bmi, 2))
		print("That would be considered underweight")

	if 18.5 <= bmi <= 25:
		print("You have a BMI of ", round(bmi, 2))
		print("That would be considered normal weight")

	if 25 <= bmi <= 30:
		print("You have a BMI of ", round(bmi, 2))
		print("That would be considered overweight")

	if bmi > 30:
		print("You have a BMI of ", round(bmi, 2))
		print("That would be considered obese")

# Print out if user enters incorrect input
except ValueError:
	print("Are you sure you entered correct values for height and weight?")
	print("Please try again")