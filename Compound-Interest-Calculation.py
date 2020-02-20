principal = 1000 #variable declaration
rate = 0.05; numYears = 5 ; year = 1 #can have multiple variable declaration in single line provided seperated by ;;;;;;;

# while statement
while year <= numYears:
    principal = principal *(1+rate)
    print ("%3d %0.2f" % (year, principal))
   # print format(year, "3d"), format(principal, "0.2f")
    year +=1

# if Condition
a = 5; b = 4

if a < b:
    print "Computer says Yes"
else:
    print "Computer says No"

# Boolean express using or, and or not
product = "game"
type="pirate memory"
age = 9
# backslash (\) allows to write code at next line
if product == "game" and type == "pirate memory" \
        and not (age<4 or age > 8):
    print "i'll take it!"


# if else statement
# Python does not have switch or case statement
suffix = ".htm"
if suffix == ".htm":
    content = "text/html"
elif suffix == ".jpg":
    content ="image/jpeg"
elif suffix==".png":
    content="image/png"
else:
    raise RuntimeError("Unknown content type")

# File input and Output
f = open("c:/AB/foo.txt","w") # returns a new file object for reading
while year <= numYears:
    principal = principal *(1+rate)
    f.write("%3d %0.2f" % (year,principal))
    f.write("111111");
    #print("%3d %0.2f" % (year,principal),file=f)
    # print format(year, "3d"), format(principal, "0.2f")
    year +=1
f.close()

f = open("c:/AB/foo.txt") # returns a new file object for reading
line = f.readline() # invokes readline() method on file
while line:
    print line, #',' omits newline character
    line = f.readline()
f.close()

str = "Hello World"
print str[1] # print char from string at given location
print str[1:5] # print range of char from string

