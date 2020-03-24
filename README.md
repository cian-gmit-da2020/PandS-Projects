# PandS-projects
# Cian Hogan
# HIGHER DIPLOMA IN SCIENCE IN COMPUTING (DATA ANALYTICS)
# Programming and Scripting Module, Projects Repository

Table of contents
1. bmiCalc.py
2. revString.py
3. collatz.py
4. weekday.py
5. sqroot.py
6. letterCount.py
7. plotty.py

# 1. bmiCalc.py, BMI calculator

- This programme takes an input from the user and assigns those values to the variables **height and weight**.
- The programme then applys a standard bmi formula to those variables and stores that value in the variable **bmi**
- The programme finishes by printing a message to the screen which includes the value bmi rounded to two decimal places

# 2. revString.py

- This programme takes a string input from the user.
- Using string slicing and a print statement the programme prints the string to the screen stepping backwards through the string two characters at a time

# 3. collatz.py

- This programme takes an input from the user of a positive number and performs a calculation on that number until it reaches one.
- The programme performs a different calculation whether the number is even or odd.
- First a try/except block is placed which will print a message to the screen if the user does not enter a number value as their input.
- Next the programme checks to ensure that the user has entered a positive number and will return a message if they have not.
- A while loop ensures the programme will continue to run provided the number remains not equal to one.
- The programme then checks for odd or evenness and applies the correct action to the number depending on the result.

# 4. weekday.py

- This programme uses the datetime module to check the current day of the week and prints different message to the screen if its a weekday or a weekend.
- The programme begins by importing the **datetime** module
- The programme creates a variable for todays day index using datetimes **now() and weekday()** methods
- A list of all the days in order is created
- The programme checks the index of today to determine if its a weekday or not and prints an appropriate message depending on the result

# 5. sqroot.py

- This programme defines a funtion **sroot()** for estimating the square root of any positive number
- The programme uses an infinite loop with break statements that end the loop at certain points when certain conditions have been met
- First the function finds the closest whole root number to the input value
- Then the function uses [newtons square root method](https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf) to get a much closer approximation of the square root value and returns that value ending the fuction
<img src="https://render.githubusercontent.com/render/math?math=x_n+1 = {1}{2}(x_n + {a}{x_n})">
- The programme then asks the user for an input value to calculate the square root of, variable **i**
- Then the programme calls the function of the variable i and stores the result in the variable **iroot**
- The programme then prints the value of iroot rounded to 2 decimal points.

# 6. letterCount.py, also includes mobydick.txt

- This programme uses command line arguments to open and read a file and return a count of characters in the file
- The programme imports the sys module and uses the fuction argv to access the command line arguments
- The programme assigns the second command line argument as the string value to use for the filename
- The programme sets the search variable **letter** to default **e**
- The programme checks to see if the user has entered a third command line argument and if that argument is a single charachter then it updates the search letter variable to the argument
- Using a **with** block, the prgramme opens the file **fname** and iterates over every character in each line counting how many times **letter** appears
- Finally the program prints a formatted string to the screen containing the results of the search

# 7. plotty.py

- This programme plots 3 seperate functions on a single plot
- **f(x) = x**, **g(x) = x<sup>2</sup>** and **h(x) = x<sup>3</sup>**
- The programme starts by importing the numpy and matplotlib's pyplot module
- Using numpy's **linspace** method the programme creates an array of 100 equally spaced values between **0** and **4**
- using linspace allows for a smoother graph that more accurately mirrors the actual function
- The programme creates 3 seperate plots, one for each function and assigns a colour and label to each plot
- The programme adds a label to the x & y axis, a legend and a title for the plot
- The **plt.show()** method displays the plot to the screen 
