#Try and except statements
try:
    f = open('too.txt')
except IOError as e:
    print("Unable to open 'foo' :",e)

# Multiple Try and except statements
try:
    f = open('too.txt')
except IOError as e:
    print("Unable to open 'foo' :",e)
except Exception as e: # This catches all exception thrown by code
    print("Unable to open 'foo' :",e)


#Try and except statements with else
try:
    f = open('too.txt')
except IOError as e:
    print("Unable to open 'foo' :",e)
else:
    data = f.close()
    print("Sorry it did not work out")

#Try and except statements with finally block
try:
    f = open('too.txt')
except IOError as e:
    print("Unable to open 'foo' :",e)
finally: # finally statement defines a cleanup action for code contained in try catch block
    data = f.close()
    print("Sorry it did not work out")