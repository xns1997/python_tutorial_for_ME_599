import numpy as np
import matplotlib.pyplot as plt
import random as random
from scipy.optimize import fmin
import scipy.optimize as opt
from inspect import signature

def f(x):
    return -x ** 2 - 3 * x + 6

def optimize_step(f,bounds_a,bounds_b,n):
    if bounds_a < bounds_b:  # Judge the bounds value
        bounds_low, bounds_up = bounds_a, bounds_b
    else:
        bounds_up, bounds_low = bounds_a, bounds_b
    x = np.linspace(bounds_low,bounds_up,n)
    largest_value1 = x[0]

    for i in range (len(x)-1):
        if f(x[i]) <= f(x[i+1]):
            largest_value1 = x[i+1]
        #print(largest_value1)
        #plt.plot(f(x), '-x', label="Function Plot")
    return largest_value1

def optimize_random(f,bounds_a,bounds_b,m):
    if bounds_a < bounds_b:  # Judge the bounds value
        bounds_low, bounds_up = bounds_a, bounds_b
    else:
        bounds_up, bounds_low = bounds_a, bounds_b
    largest_value2 = (bounds_low+bounds_up)/2
    #print(largest_value2)

    for i in range (m):
        x = random.uniform(bounds_low, bounds_up)
        if f(x) - f(largest_value2) >= 0:
            largest_value2 = x
        #plt.plot(f(x), '--x', label="Function Plot")
    return largest_value2

#Use the Python optimization function fmin to calculate the max value
def fmax(x):
    return float(0 - f(x))

def optimize_fmax(fmax,bounds_a,bounds_b):
    if bounds_a < bounds_b:  # Judge the bounds value
        bounds_low, bounds_up = bounds_a, bounds_b
    else:
        bounds_up, bounds_low = bounds_a, bounds_b
    largest_value3 = fmin(fmax,(bounds_low+bounds_up)/2,disp=0)[0]
    num_itera = fmin(fmax, (bounds_low + bounds_up) / 2, disp=0,full_output=1)[2]

    if largest_value3 <= bounds_low or largest_value3 >= bounds_up:
        if fmax(bounds_low) >= fmax(bounds_up):
            largest_value3 = (bounds_up)
        else:
            largest_value3 = (bounds_low)
    return largest_value3,num_itera

#that optimizes a multidimensional function
def fmult(a,b,c,d,g):
    return a**2+b**3*c-d*g

def optimize_md(fmult,bounds):
    n = len(signature(fmult).parameters)
    m = len(bounds)
    if n != m:
        raise ValueError
    elif n == 1:
        bounds = [bounds]

    def fm(X):
        return -fmult(*X)
    x_cons_opt = opt.minimize(fm, np.array(bounds)[:,0], method='L-BFGS-B', bounds=bounds).x
    return x_cons_opt

if __name__ == '__main__':
    maxvalue1 = optimize_step(f, -10, 100, 5000)
    print('optimize_step:',maxvalue1)
    maxvalue2 = optimize_random(f, -10, 100, 5000)
    print('optimize_random:',maxvalue2)
    maxvalue3,numit = optimize_fmax(fmax,-10,100)
    print('optimize_fmax:',maxvalue3)
#test two functions and the Python optimization function, testing function is -x ** 2 - 3 * x + 6
# and the max value is (-1.5,8.25)
    di1 = []
    di2 = []
    di3 = []
    n = [ii for ii in range(10, 300, 20)]
    # print(n)
    for i in n:
        maxvalue1 = optimize_step(f, -10, 100, i)
        maxvalue2 = optimize_random(f, -10, 100,i)
        maxvalue3 = optimize_fmax(fmax, -10,100)
        di1.append(abs(maxvalue1 - (-1.5)))
        di2.append(abs(maxvalue2 - (-1.5)))
        di3 = (abs(maxvalue3[0] - (-1.5)))
        #print(di3)
    plt.plot(n, di1, '-x', label="the error between optimize_step and testing function")
    plt.plot(n, di2, '--x', label="the error between optimize_random and testing function")
    plt.plot(numit,di3, '-rx', label="the error between optimize_fmax and testing function")
    plt.xlabel('Numbers')
    plt.ylabel('Difference Value')
    plt.legend()
    plt.title('Absolute difference of functions Plots')
    plt.show()
#test multidimensional functions
bounds = [(-2, 10), (-6, 9),(-4,9),(-2,11),(2,5)]
maxmu = optimize_md(fmult,bounds)
print('multidimensional-function max value:',maxmu)
