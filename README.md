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
8. References

# 1. bmiCalc.py, BMI calculator

[BMI wiki](https://en.wikipedia.org/wiki/Body_mass_index) [1]  
<img src="https://render.githubusercontent.com/render/math?math=BMI = \frac{weight}{height^2}">

*bmiCalc.py takes inputs from the user of their height in Meters and weight in Kilograms and calculates their BMI score and returns the result*

- The programme begins by defining a function called checkBMI which takes a single input of a number and returns a different message depending on the value of the input.
- These messages correspond to the different classifications of BMI (underweight, normal, overweight and obese).
- The programme implements a **[try/except](https://docs.python.org/3/tutorial/errors.html)**[2] code block to ensure inputs numerical values for height and weight.
- If the input is incorrect (for example if the user passes a word in) the exception will tell the user why it has failed.
- Then the programme takes an input from the user and assigns those values to the variables **height and weight**.
- The programme then applies the standard bmi formula shown above to those variables and stores that value in the variable **bmi**
- The variable bmi is the passed to the function checkBmi which prints out its result.

# 2. revString.py

*revString.py takes an input of a sentence of any length from the user and prints every second character of that sentence back to the screen in reverse*

- This programme takes a string input from the user and stores it in the variable **string**.
- Using **[string slicing](https://realpython.com/lessons/string-slicing/)**[3] and a print statement the programme prints the string to the screen stepping backwards through the string two characters at a time

# 3. collatz.py
[Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)[4]

*collatz.py takes an input of any positive integer from the user and performs the collatz process (linked above) of dividing the value by two if it is **even** but if the value is **odd**, multiplying it by three and adding one. As the process executes the programme prints each new value to the screen until it reaches 1 and the programme finishes* 

- The programme starts with a **try/except** block to make sure the user enters a correct integer value. If the value is not an integer the programme prints an exception message to the screen.
- The programme then takes an input from the user and then checks to make sure it is a positive number, If the number is negative a message will print to the screen and the programme will end.
- The original value is printed to the screen before any calculations are done. The print statement uses a second argument **end=" "** so the programme will not automatically insert newline characters and instead will print all values on the same line.
- The programme then performs a different calculation whether the number is even or odd.
- A while loop ensures the programme will continue to run provided the number remains not equal to one.
- The programme then checks for odd or evenness and applies the correct action to the number depending on the result.
- At the end of each loop the updated value in printed to the screen, again using the **end=" "** argument.
- The programme ends when the value reaches 1.

# 4. weekday.py

*This programme uses the datetime module to check the current day of the week and prints different message to the screen if its a weekday or a weekend.*

- The programme begins by importing the **[datetime](https://docs.python.org/3/library/datetime.html)**[5] module.
- The programme creates a variable **day** for today's day index using datetime's **now() and weekday()** methods.
- A list named **days** is created of all the days of the week in order Mon-Sun.
- The programme then checks the index of today to determine if it's a weekday or not and prints an appropriate message depending on the result.

# 5. sqroot.py
[newtons square root method](https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf)[6]
<img src="https://github.com/cian-gmit-da2020/PandS-Weekly-Projects/blob/master/Square%20root%20equation.png?raw=true">

*sqroot.py takes any floating-point number as an input and calculates an approximation of that input value's square root. Then it prints that square root value to the screen, rounded to 2 decimal points.*

- This programme starts by defining a function **sroot()** with input variable **X**. The function the estimates the square root of the input **X**.
- The function uses an infinite loop with break statements that end the loop at certain points when certain conditions have been met
- First the function finds the closest whole root number to the input value.
- The function initialises a counter variable named **count**.
- The function checks in count<sup>2</sup> is equal to x, if it is then count is the square root of X and the function is complete.
- If count is not the square root of X the function checks if count<sup>2</sup> is less than X. If count<sup>2</sup> is less than X, count is incremented by 1 and the loop repeats.
- If count<sup>2</sup> is greater than X then we know the square root of X is between count and count - 1.
- The value of count is assigned to the variable **root**.
- A while loop ensure that the next section of code will continue until root<sup>2</sup> is equal to X, *within two decimal places*.
- Then the function uses **Newton's square root method**, above, to get a much closer approximation of the square root value and returns that value ending the function.
- The second half of the programme takes input from the user and returns a square root value.
- The programme starts with a **try/except** block to make sure the user enters a correct numerical value. If the value is not a number the programme prints an exception message to the screen.
- The programme asks the user for an input value to calculate the square root of, and assigns it to the variable **i**
- Then the programme calls the function sqroot on the variable i and stores the result in the variable **iroot**
- The programme then prints the value of iroot rounded to 2 decimal points.

# 6. letterCount.py, also includes mobydick.txt
[Moby Dick Text File](https://www.gutenberg.org/files/2701/old/moby10b.txt)[7]

*This programme uses command line arguments to open and read a file and return a count of characters in the file.*

- The programme starts by importing the **[sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys)** module.
- The programme uses a **try/except** block to make sure to check the users arguments are correct. If the user doesn't enter enough arguments for the programme to function a specific message will print to the screen. If there are enough arguments but there is any issues with the filename or the file doesn't exist a specific message will print to the screen. 
- The next a variable **fname** is initiallised and it is assigned the string value of the second item in the list **sys.argv** as its value.
- The programme sets the search variable **letter** to default **e**.
- The programme checks to see if the user has entered a third command line argument and if that argument is a single character then it updates the search letter variable to the third argument.
- Using a **with** block, the programme opens the file **fname**. A counter variable **count** is initialised and its value set to 0.
- The programme then iterates over every character in each line. If the value in **letter** appears, the count is incremented by 1.
- When the programme has gone through the entire file it prints a formatted string to the screen containing the results of the search.

# 7. plotty.py 

*This programme plots 3 separate functions of **X** on a single plot.*
**f(x) = x**, **g(x) = x<sup>2</sup>** and **h(x) = x<sup>3</sup>**

- The programme starts by importing the **[numpy](https://numpy.org/)**[8] and **[matplotlib](https://matplotlib.org/)'s pyplot**[9] modules.
- Using numpy's **linspace** method the programme creates an array of 100 equally spaced values between **0** and **4**.
- Using linspace allows for a smoother graph that more accurately mirrors the actual functions.
- Using pyplot method **[subplots()](https://realpython.com/python-matplotlib-guide/)**[10] the programme initialises the variables **fig and ax** which are the plot **Figure and Axes objects**. 
- The programme creates 3 separate line plots on the same Axes, ax. One plot for each function f(x),g(x) and h(x) and assigns a colour and label to each plot.
- The programme adds a label to the x & y axis, a legend, a grid and a title for the plot ax.
- The **fig.show()** method displays the plot to the screen.
- A final **input()** call is added to keep the programme running while the plot is displayed on the screen. The programme will only close if the user enters an input to the command line.

# References

1. https://en.wikipedia.org/wiki/Body_mass_index
2. https://docs.python.org/3/tutorial/errors.html
3. https://realpython.com/lessons/string-slicing/
4. https://en.wikipedia.org/wiki/Collatz_conjecture
5. https://docs.python.org/3/library/datetime.html
6. https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
7. https://www.gutenberg.org/files/2701/old/moby10b.txt
8. https://numpy.org
9. https://matplotlib.org
10. https://realpython.com/python-matplotlib-guide/


