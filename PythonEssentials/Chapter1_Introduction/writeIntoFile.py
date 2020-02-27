f = open("foo.txt","w") #open file for writting

principal  = 1000 # Initial amount, this is an integer data type
rate = 0.05 # Interest rate
numyears = 5 # number of years
year = 1

while year <= numyears:
    principal = principal*(1*rate)
    f.write("%3d %0.2f\n" % (year,principal)) #File output
    #print ("%3d %0.2f" % (year, principal))
    #print (year, principal)
    year = year+1
f.close()