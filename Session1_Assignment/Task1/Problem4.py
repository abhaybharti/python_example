# ----  Problem Statement -----
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3

diameter = int(input("Enter diameter to calculate Volume of Sphere : ")) # take diameter as input from user
print ("Diameter entered : "+str(diameter)) #Print diameter value on console
radius = int(diameter/2) # derive radius value
print ("Radius : "  +str(radius)) # print radius value
volume = (4/3)*3.14*(pow(int(radius),3)) # calculated volume of Sphere
print("Volume of Sphere : "+str(volume)) #print volume

#--- Output ---
# Enter diameter to calculate Volume of Sphere : 12
# Diameter entered : 12
# Radius : 6
# Volume of Sphere : 904.3199999999999
