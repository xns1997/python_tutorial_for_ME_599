# Lab 7
* Due Friday by 11:59 pm, Mar. 1
* Submitting a file py.
* Point 10

## Purpose
The main aim of this lab is to get you to write some simple optimization code, and to use some of the python skills you've learned up to this point.

## Assignment
* 1. Write a function, called optimize_step, the finds the largest value of a function, between a set of bounds when called like this:
```python
      x = optimize_step(f, bounds, n)
```
where f is the function, bounds is a tuple specifying the lower and upper bounds, and n is the number of steps. This function should start at the lower bound, and take n evenly-spaced evaluations of f, returning the x value of the largest one.

* 2. Write another function, optimize_random that takes the same arguments, but uses n random samples between the bounds.

* 3. Compare the accuracy of your two functions and the Python optimization function fmin (Links to an external site.)Links to an external site., on a couple of different functions.  Graph the performance of the three approaches as a function of the number of function evaluations you make.  Extra Credit: Figure out how many function evaluations the built-in Python function is making, and use it on the plot.

* 4. Write a final function, optimize_md, that optimizes a multidimensional function.  Given a function that looks like:def f(x, y, z): you should be able to call your function like this:x = optimize_md(f, bounds).  The function should return a tuple corresponding the the maximal point.  In the 3D example here, what might be (1.2, 2.2, 3.1).  The argument bounds should be a list of tuples, each tuple being the bounds along a single axis.  For example:
```python
      def f(a, b, c, d):
  ... some code ...

print optimize_md(f, [(-1, 1), (-2, 2), (2, 4), (0, 2)])
(0.4, 1.3, 1, 1)
```

## Thoughts
* 1. Gradient ascent is an idea from optimization.  The basic idea is to pick a point on the x axis, estimate the direction (left or right) in which the function increases (the gradient), and then take a step in that direction.  If you had the functional form, then you could analytically calculate the gradient.  If not, then you can evaluate the function on each side of the x you choose, see which is larger, and then take a step in that direction (and repeat until you can't go up any more).

* 2. For the extra credit question, think about how you define the function you're evaluating, and whether or not it's really a function.  Think about encapsulation and some of the examples we covered in class.

* 3. For the last function, you can give optional additional arguments, but it needs to work with just the two we specify above.

* 4. In all of the code for this assignment, try to make the functions as compact as possible, and use as much of the built-in python functionality as you can.

## Grading
- [ ] 1. Stepwise function works (1 point) and returns correct value (1 point).  [2 points total]
- [ ] 2. Random function works (1 point) and returns correct value (1 point). [2 points total]
- [ ] 3. Gradient function works (1 point), implements gradient correctly (1 point), stops correctly (1 point), and returns correct value (1 point).  [4 points total]
- [ ] 4. Code generates appropriate graphs.  [2 points total]
- [ ] 5. Extra Credit: Code that calculates how many function evaluations fmin is making. [2 points]
- [ ] 6. Multi-dimensional optimizer works (1 point) and returns correct value (1 point). [2 points total]

## What to Turn In
* A single file, called optimize.py that, when run displays your graphs, and contains the functions described above.
