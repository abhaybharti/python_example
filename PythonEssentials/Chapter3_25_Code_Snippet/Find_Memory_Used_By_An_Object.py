#The standard library’s sys module provides the getsizeof() function.
# It accepts an object, calls the object’s sizeof() method, and returns the result
import sys
print(sys.getsizeof(5)) # 28
print(sys.getsizeof("Python")) # 55