import matplotlib.pyplot as plt
import numpy as np
import math


x = [10**i for i in range(10)]

y_lin = [8*i for i in x]
y_nlogn = [4*i*math.log2(i) for i in x]
y_quad = [2*i**2 for i in x]
y_cube = [i**3 for i in x]
# y_exp = [2**i for i in x]

plt.plot(x, y_lin, label='lin')
plt.plot(x, y_nlogn, label='nlogn')
plt.plot(x, y_quad, label='quad')
plt.plot(x, y_cube, label='cube')
#plt.plot(x, y_exp, label='exp')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

# R3.2 -> n = 16

# R-3.23 O(n)
# R-3.24 O(n)
# R-3.25 O(n²) ??
# R-3.26 O(n) ??
# R-3.27 O(n³) 
