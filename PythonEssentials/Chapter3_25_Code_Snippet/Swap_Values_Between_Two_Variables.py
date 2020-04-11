#Swap two variable using temporary variable
x = 5
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#Simple Construct to swap variables
a = 5
b = 10
a,b = b,a
print('The value of x after swapping: {}'.format(a))
print('The value of y after swapping: {}'.format(b))

a = "abhay"
b = "Prabha"
a,b = b,a
print('The value of x after swapping: {}'.format(a))
print('The value of y after swapping: {}'.format(b))
