#!/usr/bin/python3

"""
Project: Self-customed complex number object and roots object
File Name: complex.py
Author: Jialu Huang
Course - Sec#: ME 599_030
Instructor: William Smart
Date: Feb 10, 2019
"""

from clear_console import clean_the_console

"""
Name: Complex
Description: Generate a object to store, print, and calculate complex numbers
Format: (real +- imag * i) 
"""
class Complex:
    #Constructor of this class when default parameters are 0s
    def __init__(self, real = 0, imag = 0): 
        self.real = real
        self.imag = imag
    #define formatted print
    def __repr__(self):
        com_str = ""
        com_str += "(" + "%s" % ("%g" % self.real) + num_to_str(self.imag) + "i)"  #%+-g means display sign
        return com_str
    #define formatted string for print()
    def __str__(self):
        return self.__repr__()
    
  #output format is not very clearly. 
    
    
    #Overloading operator + OR plus
    def __add__(self, o):     #(binary +)
        if isinstance(o, (float,int)):    #Make sure the type of operands between the operator are the same.
            o = Complex(o)
        return Complex(self.real + o.real, self.imag + o.imag) #return as a new assigned complex object

    def __radd__(self, o):          #Solve some equations have a wrong data type at the left side of operator 
        return self.__add__(o)

    def __sub__(self, o):     #(binary -)
        if isinstance(o, (float,int)):    #Make sure the type of operands between the operator are the same.
            o = Complex(o)
        return Complex((self.real - o.real),(self.imag - o.imag))
    
    def __rsub__(self,o): 
        return self.__sub__(o)

    def __mul__(self, o):    #(binary *)
        if isinstance(o, (float,int)):    #Make sure the type of operands between the operator are the same.
            o = Complex(o)
        return Complex(((self.real * o.real)+ (-1)*(self.imag * o.imag)),(self.real * o.imag)+(self.imag * o.real))
    
    def __rmul__(self, o):
        return self.__mul__(o)

    def __truediv__(self, o):    #(binary /)
        if isinstance(o, (float,int)):    #Make sure the type of operands between the operator are the same.
            o = Complex(o)
        a = (self.real * o.real) + (self.imag * o.imag)
        b = pow((o.real), 2.0) + pow((o.imag), 2.0)
        c = (self.imag * o.real) - (self.real * o.imag)
        return Complex((a / b),(c / b))
    
    def __rtruediv__(self, o):  # self/o and o/self are different
        temp = Complex(o)
        return temp.__truediv__(self)

    def __neg__(self):            #Get negative complex number (unary -)
        return Complex(0 - self.real, 0 - self.imag)

    def __invert__(self):         #Get conjugate complex number (unary ~)
        return Complex(self.real, 0 - self.imag)
    
    def __eq__(self, o):   #(Binary ==) Determine that the two Complex objects are completely equal
        if self.real == o.real and self.imag == o.imag:
            return True
        else:
            return False

def num_to_str(num):
    if(num >= 0):
        return " + " + str(num)
    else:
        return " - " + str(abs(num))


def div_line():
    print(50 * "/")


if __name__ == '__main__':
    clean_the_console()
    a = Complex (1,2)
    b = Complex (3,-4)
    print(a,b)

    print(a, " + ", b," = ", a + b)
    print(a, " - ", b," = ", a - b)
    print(a, " * ", b," = ", a * b)
    print(a, " / ", b," = ", a / b)
    div_line()
    print(a, " + ", 1.5, " = ", a + 1.5)
    print(1.5, " + ", a, " = ", 1.5 + a)

    print(a, " - ", 1.5, " = ", a - 1.5)
    print(1.5, " - ", a, " = ", 1.5 - a)

    print(a, " * ", 1.5, " = ", a * 1.5)
    print(1.5, " * ", a, " = ", 1.5 * a)

    print(a, " / ", 1.5, " = ", a / 1.5)
    print(1.5, " / ", a, " = ", 1.5 / a)

    div_line()
    print("Negation",-a)
    print("conjugate",~a)
    print("a = b ? -> ",a == b)
    
    div_line()
    c = Complex()
    d = Complex(3,)
    print (c,d)
    print(c, " + ", d," = ", c + d)
    print(c, " - ", d," = ", c - d)
    print(c, " * ", d," = ", c * d)
    print(c, " / ", d," = ", c / d)
