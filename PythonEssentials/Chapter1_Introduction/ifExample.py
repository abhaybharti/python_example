a=10
b=20

####################################################
#Simple If test
####################################################
if a<b:
    z=b
else: # else is optional
    z=a
print (z)

####################################################
#To create an empty clause, use the pass statement
####################################################
a=11
b=12
t = 0
# Simple if test
if a<b:
    pass #To create an empty clause, use the pass statement
else:
    t=a
print (t)

####################################################
# Form Boolean expression using or, and and not keywords
####################################################
c = 5
if b >= a and b <=c:
    print ("b is between a and c")
if not (b < a or b > c):
    print ("b is still between a and c")

####################################################
# Use elif statment to handle multiple tests
####################################################
a = "*"
if a == '+':
    op = "PLUS"
elif a == '-':
    op = "MINUS"
elif a == '*':
    op = "MULTIPLY"
else:
    raise RuntimeError("Unknow operator")
print (op)