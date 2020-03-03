# ----  Problem Statement -----
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

from pip._vendor.distlib.compat import raw_input

str = str (raw_input("Enter comma separated integer value: ")) # take comma seperated input from user
print ("Input string: ", str)


list = str.split (",") # Generate list
print ("list: ", list)

# --- Output ---
# Enter comma separated integer value: ab , cvb, python, java
# Input string:  ab , cvb, python, java
# list:  ['ab ', ' cvb', ' python', ' java']