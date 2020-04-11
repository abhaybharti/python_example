principal  = 1000 # Initial amount, this is an integer data type
rate = 0.05 # Interest rate
numyears = 5 # number of years
year = 1

while year <= numyears:
    principal = principal*(1*rate) # here float value is getting reassigned, principal variable changed to float data type
    print ("%3d %0.2f" % (year, principal))
    #print (year, principal)
    year = year+1

"""This is also a
dfdfdf
dfdfd"""

'''This is also a
dfdfdf
dfdfd'''