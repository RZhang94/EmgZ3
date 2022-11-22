import numpy as np
import scipy as sp
from scipy.optimize import fsolve
from scipy.optimize import leastsq

def func(x, y):
    jacobian = [x[0] * x[1] - y[0], x[0] + x[1] -y[1]]
    return jacobian

y = [1,2.2]

root = fsolve(func, [0,0], args = y)
print(root)

def func2(x, y):
    jacobian = [x[0]**2 * x[1] + x[2] - y[0], - x[0] * x[2] + x[1] -y[1], x[0] * x[1] * x[2] - y[2]]
    return jacobian

y = [5, -1, 6]

root2 = fsolve(func2, [0,0,0], args = y)

print(root2)

root3 = leastsq(func2, [0,0,0], args = y)

print(root3)

print('hi')