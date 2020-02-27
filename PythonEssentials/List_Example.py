#Lists - can contain any kind of python object including other list
#create an empty list
names = []
names = list()
names = ["Dave","Mark","Ann","Phil"] # create a list
print (names[2]) # Fetch list element
names[0] = "AB" # change first item to "AB"
print (names)

names.append("Paula") #add new items to end of list
print (names)
names.insert(2,"BA")
print (names)  # insert new element at index 2

print (names[0:2]) # returns 0 to 2 index items
print (names[2:]) # returns item starting from index 2 till end

# + operator to concatenate two lists
a = [1,2,3]+[4,5]
print (a) # resutl is [1,2,3,4,5]

# Nested lists
a = [1,"Dave",3.14, ["Mark",7,9,[100,101]], 10]
print (a[1])
print (a[3])
print (a[3][2])
print (a[3][3][0])

# Advance List features

import sys # load the sys module

if len(sys.argv)!= 2: # check number of command line arguments
    print ("Please supply  a filename")
    raise SystemExit(1)
f = open(sys.argv[1]) #Filename on the command line
lines = f.readline() # read all ines into a list
f.close()
