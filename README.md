### Project Overview

 Task 1:
Define a class called complex_numbers which accepts 2 parameters:
real: int64, float64, represents real component of the complex number
imag: int64, float64, represents imaginary component of the complex number
Example, complex_numbers(3, 5) means 3 is the real part of the complex number and 5 is the imaginary part of the complex number. Such a number is represented as 3 + 5i.

Implement the above using __init__ function.

The __repr__ function is given to you. Add that to the class and then try implementing "print()" statement to one of the class created objects.

def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

New Concept: Operator Overloading
Input

2 +3
Output

5
Input

'New' +'York'
Output

'NewYork'
+ operator adds numbers and at the same time concatenates strings. That is because + operator is overloaded by both int class and str class. The operators are just methods defined in their respective classes.

Defining methods for operators is known as operator overloading. For e.g. To use + operator with custom objects, you need to define a method called add .

Task 2:
Define the following operations for the class by implementing operator overloading.

'+' (complex number addition)

The sum of two complex numbers C= a+ ib and C'= a' + ib' is

complex_add

- Create a function called __add__ which takes two parameters 'self' and 'other'

- Inside the function, should be statements performing complex number addition and storing the results in appropriate variables(Different variables for real part and imaginary part of the sum)

- The function should return both the above created variables enclosed as complex number object. For eg: If the variables to return are a & b, the return statement should be 
"return complex_numbers(a,b)"
'-' (complex number subtraction)

The difference between two complex numbers C= a+ ib and C'= a' + ib' is

complex_diff

- Create a function called __sub__ which takes two parameters 'self' and 'other'

- Inside the function, should be statements performing complex number subtraction and storing the results in appropriate variables(Different variables for real part and imaginary part of the difference)

- The function should return both the above created variables enclosed as complex number object
'*' (complex number multiplication)

The product of two complex numbers C=a+ ib and C'= a' + ib' is

complex_prod

The special case of a complex number C=a+ ib multiplied by a scalar a' is

complex_prod2

- Create a function called __mul__ which takes two parameters 'self' and 'other'

- Inside the function, should be statements performing complex number multiplication and storing the results in appropriate variables(Different variables for real part and imaginary part of the product)

- The function should return both the above created variables enclosed as complex number object
'/' (complex number division)

The division of two complex numbers C= a+ ib and C'= a' + ib' is done by multiplying the numerator and denominator by the complex conjugate of the denominator

complex_quot

Create a function called truediv which takes two parameters 'self' and 'other'.

Inside the function, should be statements performing complex number division and storing the results in appropriate variables(Different variables for real part and imaginary part of the quotient)

The function should return both the above created variables enclosed as complex number object

Note: These operations should be compatible with int and float datatypes as well

Task 3:
Define the following methods inside the class(These are not operation overload methods).

absolute() function that returns absolute value of the complex number
The absolute value of the complex number C= a+bi is the distance between the origin (0,0) and the point (a,b) in the complex plane

comp_abs

   - Create a function called abs which takes one parameter 'self'.

    - Inside the function, should be statements finding out the absolute value of the complex number and storing the result in an appropriate variable

    - The function should return the above created variable
argument() that returns argument of the complex number

The argument of a complex number C=a+ ib is defined by this

But for this task you can simply take it as,

complex_arg

   - Create a function called argument which takes one parameter 'self'.

    - Inside the function, should be statements finding out the argument of the complex number and storing the result in an appropriate variable

    - The function should return the above created variable
conjugate() that returns conjugate of the complex number

The conjugate of a complex number is the number with the same real part and an imaginary part equal in magnitude but opposite in sign

complex_conj

Create a function called conjugate which takes one parameter 'self'

Inside the function, should be statements performing finding the conjugate of complex number and storing the results in appropriate variables(Different variables for real part and imaginary part of the quotient)

The function should return both the above created variables enclosed as complex number object

Task 4:
After creating a class with all the above methods, let's create objects and implement its methods.

Create an object with real part=3, imaginary part=5 and save it in a variable called 'comp_1'

Create an object with real part=4, imaginary part=4 and save it in a variable called 'comp_2'

Implement addition of 'comp_1' and 'comp_2' and save the sum in a variable called 'comp_sum'

Implement subtraction of 'comp_1' and 'comp_2' and save the difference in a variable called 'comp_diff'

Implement multiplication of 'comp_1' and 'comp_2' and save the product in a variable called 'comp_prod'

Implement division of 'comp_1' and 'comp_2' and save the quotient in a variable called 'comp_quot'

Find the absolute value of comp_1 and save it in a variable called comp_abs

Find the conjugate value of comp_1 and save it in a variable called comp_conj

Find the argument value of comp_1 and save it in a variable called comp_arg


### Learnings from the project

 1) Function overloading
2)Operator Overloading
3) Class
4) Functions
5) using of class objects


