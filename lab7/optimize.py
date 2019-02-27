#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2 - 3 * x + 6

def optimize_step(f,bounds_low,bounds_up,n):
    x = np.linspace(bounds_low,bounds_up,n)
    #print(x)
    largest_value1 = 0
    for i in range (n - 1):
        if f(x[i]) <= f(x[i+1]):
            largest_value1 = f(x[i+1])
        else:
            largest_value1 = f(x[i])
        plt.plot(f(x), '-x', label="Function Plot")
    return largest_value1

def optimize_random(f,bounds_low,bounds_up,n):
    x = np.random.uniform(bounds_low,bounds_up,n)
    largest_value2 = 0
    for i in range(n - 1):
        if f(x[i]) <= f(x[i + 1]):
            largest_value2 = f(x[i + 1])
        else:
            largest_value2 = f(x[i])
        plt.plot(f(x), '--x', label="Function Plot")
    return largest_value2

#def optimize_md():


if __name__ == '__main__':
    maxvalue1 = optimize_step(f,-6,0,10)
    print(maxvalue1)
    maxvalue2 = optimize_random(f, -6, 0, 10)
    print(maxvalue2)

    plt.xlabel('Number')
    plt.ylabel('Value')
    #plt.legend()
    plt.title('Function Plot')
    plt.show()
