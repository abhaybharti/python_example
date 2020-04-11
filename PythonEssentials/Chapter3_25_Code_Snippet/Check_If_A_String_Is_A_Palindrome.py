#Function checks if a string is a palindrome or not using slice operator
def palindrome(string):
    return string == string[::-1]

print(palindrome('python'))