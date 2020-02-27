f = open("foo.txt") #open file for reading and returns a file object
line = f.readline() # Invokes readline() method for file
while line:
    print (line,) # trailing ',' omits newline character
    line = f.readline()
f.close()