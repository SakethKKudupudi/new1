# Python program to swap two variables
x = 5
y = 10
# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
# create a temporary variable and swap the values
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#In this program, we use the temp variable to hold the value of x temporarily. 
# We then put the value of y in x and later temp in y. In this way, the values get exchanged.


#Ex2
#without using the temp variable
x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)
