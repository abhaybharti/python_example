# To create string literal, enclose them in single, double or triple quotes. The same type of quote used to start a string
# must be used to terminate it

a  ="Hello world"
b = "Python is a langauge"
c ="""What is footnote 5? """
d = 'Python is a langauge 2'
e = '''What 
is topnote''' # Triple quoted string are useful when the contents of a strings liternal span multiple lines of text

print(a)
print(b)
print(c)
print(d)
print(e)

#String are sequence of characetrs indexed by integers starting at ZERO. To extract a string, use slicing operator s[i:j]
print (a[4]) #print 5th element from string value hold by variable a
print (a[0:3]) # print element starting from 0 to 3rd
print (a[3:]) # print element starting from 3 to end

#String are concatenated with the plus (+) operator
g = a + b
print (g)

#Other dataypes can be converted to string in three ways
s = "the value of x is "+str(a) #using str conversion function
s = "the value of x is "+repr(a) #using repr() method
s = "the value of x is "+'a' # using backquotes(')


sentence = 'The dog name is samy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))