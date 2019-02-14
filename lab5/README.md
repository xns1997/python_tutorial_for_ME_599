# Lab 5
* Due Friday by 11:59pm Points <b> 12 </b>
* Submitting a file upload File Types `zip, tar, and tgz`

## Purpose
The goal of this lab is to introduce you to classes in Python, and to give you some practice writing them.

## Preparation
Remind yourself about complex numbers. Read chapters 15 and 16 in the textbook.

## Assignment
* We're going to write a class for complex numbers. Start by writing a class called Complex that takes two arguments, representing the real and imaginary parts of a complex number. Put the class definition in a file called complex.py, and call the member variables re and im. You should make these arguments optional, and default to something sensible if they are missing. Check that your code does the right thing in response to the following:
```python
     a = Complex(1.0, 2.3)    # 1 + 2.3i
     b = Complex(2)           # 2 + 0i
     c = Complex()            # 0 + 0i
```
* Implement the __repr__ and __str__() functions, so that
```python
     a = Complex(1, 2)
     b = Complex(1, -2)
     print(a)
     print(b)
```
* works and prints out
```
     (1 + 2i)
     (1 - 2i)
```
### Thoughts
* Python already has support for complex numbers.  We're going to ignore that for the purposes of this assignment.  The code you write should have the same behavior as the build-in complex number support.
* `__repr__` and `__str__` do similar things.  Python internally uses `__repr__` sometimes and `__str__` at other times.  You should implement __repr__ to return the string representation of the complex number class.  Then have `__str__` have a single line: `return self.__repr__()`
* Ensure we can get at the real and imaginary components of your Complex class like this:
```python
     c = Complex(1.2, 3.4)
     print(c.im)
     print(c.re)
```
* Implement addition, such that the following works:
```python
     a = Complex(1, 2)
     b = Complex(3, 4)
     print(a + b)
     print(a + 1)
     print(1 + a)
```
&nbsp; &nbsp; &nbsp;  and prints out
```
     (4 + 6i)
     (2 + 2i)
     (2 + 2i)
```
&nbsp; &nbsp; &nbsp; Once you have addition working, implement subtraction. This should look a lot like addition.
* Now, implement multiplication and division. Verify that everything works as expected.
* Finally, implement negation and the complex conjugate:
```python
     a = Complex(1, 2)
     print(-a)
     print(~a)
```
&nbsp; &nbsp; &nbsp; should print out
```
     (-1 - 2i)
     (1 - 2i)
```
* Extra Credit: Let's use your new class. Write a new function, in a file called roots.py, that calculates the roots of a quadratic function. You should call it like this:
```python
     roots(1, 2, 3)     # This is x^2 + 2x + 3
```
and it should return a tuple of all of the roots of the function. Sometimes these will be real numbers, sometimes they will be complex.  You should return a tuple containing all the roots you find.  Repeated roots count as one root.
## Grading
- [ ] Working constructor: 1 for each case [3 points total]
- [ ] `__repr__` and `__str__` work as described: 1 for simple case, 2 for more complex case [2 points total]
- [ ] Addition works: two complex numbers (1 point); one complex and one integer or float (1 point); one integer or float and one complex number (1 point).  [3 points total]
- [ ] Subtraction works for all three cases (like addition).  [1 point total]
- [ ] Multiplication works for all three cases (like addition).  [1 point total]
- [ ] Division works for all three cases (like addition).  [1 point total]
- [ ] Negation and complex conjugate work.  [1 point total]
- [ ] Extra Credit: Quadratic roots calculated correctly: two real roots (1 point); one root (1 point); two complex roots (1 point).  [3 points total]
## What to Hand In
A zip or tar file of your code: `complex.py`, `roots.py`, and any testing code.
## Useful Link

