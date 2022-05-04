# Find square root of real or complex numbers
# Importing the complex math module
import cmath
num = 1+2j
# To take input from the user
#num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

#Note:
# If we want to take complex number as input directly, like 3+4j,we have to use the eval() function instead of float().
#The eval() method can be used to convert complex numbers as input to the complex objects in Python. 
# To learn more, visit Python eval() function.


# Find square root of real or complex numbers
# Importing the complex math module
import cmath
num = 1+2j
# To take input from the user
#num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
