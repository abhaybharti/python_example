for n in [1,2,3,4,5,6,7,8]: # the variable n will be assigned successive items from the list on each iteration
    print (n)

print("---------------------------")
for n in range(1,10): # this short way of writting above code
    print (n)


print("-------------for loop with break--------------")
for n in range(1,10): # this short way of writting above code
    if (n == 2):
        break
    print (n)

print("-------------for loop with continue--------------")
for n in range(1,10): # this short way of writting above code
    if (n == 2):
        continue
    print (n)

print("-------------for loop with else--------------")
for n in [1,2,3,4,5,6,7,8]: # the variable n will be assigned successive items from the list on each iteration
    print (n)
else:
    print("not found")