# A set is used to contain an unordered collection of objects. To create a set, use the set() function and supply a sequence of items
s = set([3,5,9,10]) # create a set of numbers
print s
t = set("Hello") # create a set of unique characters
print t

# sets are unorderd and cannot be index by numbers and elements of a set are always unique

# set support standard collection of operation, including union, intersection, difference and symmertic difference
a = t | s # union of t and s
print a
b = t & s # intersection of s
print b
c = t - s # set difference  (item in t but not in s)
print c
d = t ^ s # Symmertic difference (item in t or s but not in both)
print d

t.add('x') # Add a single item in set
print t
s.update([11,37,42]) # Adds multipel item to s
print s

# remove item using remove() method
t.remove('H')
print t