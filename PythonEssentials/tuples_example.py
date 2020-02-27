#To create simple data structures, you can pack a collection of values together into a single object using tuple
first_name = "AB"
last_name="BA"
phone="10"
stock = ('GOOG',100,490.10)
address =('www.python.org,80')
person = (first_name, last_name,phone)

# Python recognizes that a tuple is intended even if parenthesis is missing
stock = 'GOOG',100,490.10

# For completeness, 0 and 1 element tuples can be defined.
a = () # 0- tuples (empty tuple)
b = (first_name) #1 -tuple (note the trailing comma)
c = first_name #1 -tuple (note the trailing comma)

# The values in a tuple can be extracted by numerical index just like a list, it is a common practice to unpack tuples into a set of variables
name, share, price = stock
print "======================="
print stock
print name
print share
print price

# tuple supports most of operation as list, the contents of a tuple cannot be modified after creation (you cannot replace, delete or
# append new element to an existing tuple