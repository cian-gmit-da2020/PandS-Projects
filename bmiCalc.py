# Cian Hogan week 2 task
# BMI = Weight(KG)/(Height(m)**2


# Get input from user
weight = float(input("What is your weight in Kilograms: "))
height = float(input("What is your height in Meters: "))

# work out bmi score
bmi = weight/(height**2)

# print the result
print("You have a BMI of ", round(bmi, 2))