#!/usr/bin/env python3

import numpy as np
import sys
from math import sin
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x**2
def fsin(x):
    return sin(x)

def integrate (f,a, b, n = 100):
     x = np.linspace(a,b,n)
     #print(x)
     y = []
     interval = (b - a ) / n
     print (interval)
     area  = 0
     for i in range (n):
         y += [f(x[i])]
     for i  in range (n - 1):
         #print (y[i] , y[i + 1])
         area += (y[i] + y[i + 1]) * interval / 2
     return area

def integrate_mc(f, a, b,c,d, n  = 1000):
     count = 0;
     rec_area = abs(a-b) * abs(c-d)

     for i in range (n):
         rand_x = np.random.uniform(a, b)
         rand_y = np.random.uniform(c, d)
         #if rand_y > 0:
         #  if rand_y <= f(rand_x):
         #       count += 1
         #else:
         #   if rand_y >= f(rand_x):
         #       count += 1
         if (rand_y > 0 and f(rand_x) > rand_y):
            count += 1
         elif (rand_y < 0 and f(rand_x) < rand_y):
            count -= 1
     area = rec_area * count / n
     return area

def approximate_pi(n):
    x_max = 1.0
    x_min = -1.0
    y_max = 1.0
    y_min = -1.0
    count = 0
    rec_area = abs(x_max-x_min) * abs(y_max-y_min)
    for i in range(n):
        rand_x = np.random.uniform(x_min,x_max)
        rand_y = np.random.uniform(y_min,y_max)
        if (f(rand_x)+f(rand_y)) < 1:
            count += 1
        print("Process:{0}%".format(round((i + 1) * 100 / n)), end="\r")
    print("")
    area = rec_area * count / n 
    return area

Rm= integrate(f,1,100,100000)

Mc = integrate_mc(fsin,1,100,-1,1,1000000)

print("Riemann: ",Rm)
print("MC: ",Mc)
pi = approximate_pi(100000)
print(pi)



#Calculate the definite integral by hand in python built-in function and Plot the absolute error in the approximations
w,err = quad(f,1,100)
print(w,err)

er1 = abs(w - Rm) / w
er2 = abs(w - Mc) / w
print("%.20f%%" % er1)
print( er2)

