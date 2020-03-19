# Cian Hogan
# Week nine task,  plot of the below functions of x
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# import numpy and matplotlib's pyplot module
import numpy as np
import matplotlib.pyplot as plt
 
# create an array of values for x
x = np.linspace(0, 4, 100)

# plot f(x)=x
plt.plot(x, x, "g", label="f(x) = x")
# plot g(x)=x**2
plt.plot(x, x**2, "r", label="g(x) = x squared")
# plot h(x)=x**3
plt.plot(x, x**3, "b", label="h(x) = x cubed")
# plot formatting
plt.xlabel("X")
plt.ylabel("Function of X")
plt.legend()
plt.title("Plot of f(x), g(x) and h(x)")
# show plot
plt.show()
