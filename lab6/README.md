# Lab 6
* Due: Friday 11:59 pm 22th Feb.
* Points: 12
* Submit: .py file

## Assignment
1.Write a function that will calculate and approximation of the definite integral of an arbitrary function using a Reimann sum.  The function should be in a file called integrate.py, and look like this:
```python
     i = integrate(f, a, b)
```
This should return the definite integral of the function f, from a to b.  You should also give the function an optional argument that allows the caller to specify the number of the intervals used to calculate the integral:
```python
     i = integrate(f, a, b, 100)
```
2.Write a second function that calculates the definite integral using Monte Carlo integration:
```python
     i = integrate_mc(f, a, b, (c, d), 1000)
```
Where f is the function, a and b are the bounds of the definite integral, (c, d) is a tuple such that c is lower than the lowest value of f over the interval [a, b] and d is larger than the largest value over the interval.  The last argument should be the number of Monte Carlo samples used in the approximation.

3.Pick a function and a definite integral range.  Calculate the definite integral by hand.  Plot the absolute error in the approximations of your two functions as a function of the number of intervals and the number of samples.

4.Write another function, approximate_pi(n), that approximates pi using Monte Carlo sampling.  The parameter n should specify the number of samples to use.  Use the technique we talked about in class: sample over the square that spans -1 to 1, and see what proportion of points lie within the unit circle, which has an area of pi.  The function should return the approximation.


## Thoughts
1.There is a function to do this in numpy.  You should not use it in your function, but you should consider using it for your tests.

2.You should use a Riemann sumLinks to an external site. to calculate the definite integral in the first question. There are several flavors of this, and you're free to pick any of them.  We talked about this technique briefly in class.
3.You should use Monte Carlo integration Links to an external site.for calculate the definite integral in the second question.  Again, there are several ways to do this, and you're free to pick the one you want. I'd advise starting with a simple one, using rejection samplingLinks to an external site..  The basic idea of this is to generate a sample point within the bounding box of the area (using the a, b, c, and d).  Count the number of times that this point lies within the area. The proportion of points that end up inside then lets you calculate the area, based on the area of the bounding box.  We talked about this briefly in class.

## Grading 
1. Riemann sum [4 points total] 
- [X] A Riemann sum integration function that works (1 point) 
- [ ] The function is robust to bad arguments (1 point)
- [ ] The function returns the correct answer (2 points)
2. Monte Carlo integration [4 points total] 
- [X] A Monte Carlo integration function that works (1 point), 
- [ ] The function is robust to bad arguments (1 point),
- [ ] The function returns the correct answer (2 points). 
3. Graph [2 points total] 
- [ ] A graph with appropriate labels and title (1 point) 
- [ ] The graph shows the convergence behavior of the two functions (1 point).  
4. Approximates pi [2 points total] 
- [X] A function that correctly approximates pi (2 points).  
## What To Hand In
Hand in a single file, called integrate.py, with all of your code in it.  We will import this file for our testing.  We should be able to generate your graphs by running the file as an executable.

## The rules
Everything you do for this lab should be your own work. Don't look up the answers on the web, or copy them from any other source. You can look up general information about Python on the web, but no copying code you find there. Read the code, close the browser, then write your own code.

## Useful Link
<a href="https://en.wikipedia.org/wiki/Riemann_sum">黎曼积分</a>
