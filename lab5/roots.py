#!/usr/bin/python3
"""
Project: Self-customed complex number object and roots object
File Name: roots.py
Author: Jialu Huang
Course - Sec#: ME 599_030
Instructor: William Smart
Date: Feb 10, 2019
"""


import math
from complex import Complex     #Print roots of a equation as Complex 
from clear_console import clean_the_console

"""
Name: roots
Description: Generate a object to store, print, and calculate a Quadratic equation and output all possible roots or solutions 
Format: ax^2 +- bx +- c (0 or 1 might be invisible)
"""
class roots:
    def __init__(self, a = 0, b = 0, c = 0 ):
        self.a = a
        self.b = b
        self.c = c 

        self.x1 = None   # To make sure two result varibles can store both two type of results
        self.x2 = None
    
    def __repr__(self):
        equation = "y = "  #initailized equation as a string object

        if self.a != 0:
            if (self.a != 1) and (self.a != -1):
               equation += "%s" % self.a
            elif self.a == -1:
                equation += "-"
            equation += "x" + "^2"

        if self.b < 0 :     #when b < 0 a '-' should be marked before b
            equation += " - "
            if self.b != -1:
               equation +=  "%s"%(abs(self. b))
            equation += "x"
        elif self.b > 0:
            if self.b >= 1:    # when b == 1 , '1' should not printed    #when b > 0 a '+' should be marked before b
               equation += " + "
               if self.b > 1:
                 equation +=  "%s"%(abs(self. b))
            equation += "x" 
          
        if self.c < 0 :    # Figure out operator before variable c
            equation += " - " 
        else:
            equation += " + "

        equation += "%s" % (abs(self.c))

        return equation

    def __str__(self):
        return self.__repr__()
    
    def result(self):    # the result function can solve the whole three kind of results
        delta = pow(self.b, 2.0) - 4 * (self.a * self.c)   #calculate the delta for calculation
        if delta >= 0:
            self.x1 = ((0 - self.b) + math.sqrt(delta)) / (2 * self.a)
            self.x2 = ((0 - self.b) - math.sqrt(delta)) / (2 * self.a)
            if self.x1 != self.x2:   #when delta > 0 x1 and x2 should be different
                return self.x1, self.x2
            else:        #when delta == 0 x1 should be equal to x2, so just return x1
                return self.x1
        else:    # when the delta < 0 , the equation would have two complex number roots
            delta =  4 * (self.a * self.c) - pow(self.b, 2.0) # we need a new delta 
            sqrt_delta =  math.sqrt(delta)

            self.x1 = Complex((0 - self.b)/(2 * self.a), (sqrt_delta/(2 * self.a)))
            self.x2 = Complex((0 - self.b)/(2 * self.a), (0 - sqrt_delta/(2 * self.a)))
            return self.x1 , self.x2
    

if __name__ == '__main__':
     clean_the_console()
     # two real roots
     a = roots(1,5,1)
     print("\n")
     print(a)
     print(a.result())
    #one root
     b = roots(1,2,1)
     print("\n")
     print (b)
     print(b.result())
    #two complex roots
     c = roots(2,1,1)
     print("\n")
     print (c)
     print(c.result())

     print("\n")