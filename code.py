# --------------
import pandas as pd
import numpy as np
import math
import cmath

class complex_numbers:

    #self declaration
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
    
    #for represenatation
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    #for + operator overloading
    def __add__(self,other):
        return self.real+other.real

    def __add__(self,other):
        r=self.real+other.real
        i=self.imag+other.imag
        return complex_numbers(r,i)
      
    def __sub__(self,other):
      r=self.real-other.real
      i=self.imag-other.imag
      return complex_numbers(r,i)

    def __mul__(self,other):
      r= (self.real*other.real) - (self.imag*other.imag)
      i= (self.imag*other.real) + (self.real*other.imag)
      return complex_numbers(r,i)

    def __truediv__(self,other):
      r=((self.real*other.real)+(self.imag*other.imag))/((other.real*other.real)+(other.imag*other.imag))
      i=((self.imag*other.real)-(self.real*other.imag))/((other.real*other.real)+(other.imag*other.imag))
      return complex_numbers(r,i)

    def absolute(self):
        r=math.sqrt((self.real**2)+(self.imag**2))
        return r
    
    def argument(self):
      r =math.degrees(math.atan(self.imag/self.real))
      #r=2 * (math.atan(self.imag/(math.sqrt((self.real**2)+(self.imag**2))+self.real)))
      #i=math.atan(other.real/other.imag)
      #return complex_numbers(r,i)
      r= round(r,2)
      return r

    def conjugate(self):
      r=self.real
      i=self.imag*-1
      return complex_numbers(r,i)
      #return r



comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
#obj1=complex_numbers('sagar')
#obj2=complex_numbers('bhadra')
comp_sum=comp_1+comp_2
comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=comp_1/comp_2
comp_abs=comp_1.absolute()
comp_conj=comp_1.conjugate()
comp_arg=comp_1.argument()
print(comp_sum)
print(comp_diff)
print(comp_prod)
print(comp_quot)
print(comp_abs)
print(comp_conj)
print(comp_arg)


