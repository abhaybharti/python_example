# ----  Problem Statement -----
# Write a Python program to reverse a word after accepting the input from the user.
#
# Sample Output:
# Input word: AcadGild
# Output: dilGdacA


# Solution 1. Reverse a String using slicing
strWord = input("Enter a word to reverse : ") #take input initial string
strWordLength = len(strWord) # get length of string
reversedStr = strWord[strWordLength::-1] # slicing
print (reversedStr) #printing reversed string

# Solution 2. Reverse a String using loop
reversedStr = []
strWordLength = len(strWord)  # get length of string
while (strWordLength > 0):
    reversedStr += strWord[strWordLength - 1]
    strWordLength = strWordLength - 1
print(reversedStr)  # printing reversed string

#SOlution 3 : using join
reversed=''.join(reversed(strWord)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string

# --- Ouput ---
# Enter a word to reverse : abhay
# yahba
# ['y', 'a', 'h', 'b', 'a']
# yahba
