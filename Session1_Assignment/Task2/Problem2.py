# ----  Problem Statement -----
# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Print star, start with single * keep increasing count with every iteration till loop ends
for n in range(0,5):
    for starCount in range(0,n):
       print ('*', end = '')
    print()
# Print star, start with 4 start, keep increasing count with every iteration till loop ends
for t in range(5,0,-1): # this short way of writting above code
    for starCount in range(t,0,-1):
        print ('*', end = '')
    print()


# --- Output ---
#     *
#     **
#     ***
#     ****
#     *****
#     ****
#     ***
#     **
#     *