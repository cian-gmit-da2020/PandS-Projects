# Cian Hogan
# Week nine task,  plot of the below functions of x
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# import numpy and matplotlib's pyplot module
import numpy as np
import matplotlib.pyplot as plt
 
# create an array of values for x
x = np.linspace(0, 4, 100)

# create fiq and ax plot objects
fig, ax = plt.subplots()

# plot the3 functions of x
ax.plot(x, x, "g", label="f(x) = x")
ax.plot(x, x**2, "r", label="g(x) = $x^2$")
ax.plot(x, x**3, "b", label="h(x) = $x^3$")
# customize the appearence of the plot
ax.set_xlabel("X")
ax.set_ylabel("Function of X")
ax.legend()
ax.grid()
ax.set_title("Plot of f(x), g(x) and h(x)")
# display the figure to the screen
fig.show()

# keeps the plot on the display until the user enters an input
input()
