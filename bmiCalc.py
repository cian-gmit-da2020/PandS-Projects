# BMI = Weight(KG)/(Height(m)**2
weight = float(input("What is your weight in Kilograms: "))
height = float(input("What is your height in Meters: "))

bmi = weight/(height**2)

print("You have a BMI of ", round(bmi, 2))