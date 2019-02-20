#!/usr/bin/env python3

import numpy as np
import sys
import matplotlib.pyplot as plt

def f(x):
    return x**2

def integrate (f,a, b, n = 100):
     x = np.linspace(a,b,n)
     print(x)
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

def integrate_mc(f, a, b, (c, d) ,n  = 1000):



integrate(1,100,1000)

