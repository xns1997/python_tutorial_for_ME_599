#!/usr/bin/env python3

import numpy as np
import sys
import matplotlib.pyplot as plt

def f(x):
    return x**2

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
     print(area)
     return area

def integrate_mc(f, a, b,c,d, n  = 1000):
     count = 0;
     rec_area = abs(a-b) * abs(c-d)

     for i in range (n):
         rand_x = np.random.uniform(a, b)
         rand_y = np.random.uniform(c, d)
         if rand_y < f(rand_x) and rand_y > 0 and f(rand_x) > 0:
            count += 1
         elif rand_y > f(rand_x) and rand_y < 0 and f(rand_x) < 0:
            count -= 1
     area = rec_area * count / n
     print (area)
     return area


integrate(f,1,100,100000)
integrate_mc(f,1,100,1,100000,100000)
