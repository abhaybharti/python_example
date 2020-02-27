# A dictionary is an associative array or hash table that contains object indexed by keys

# create a dictionary
stock = {
    "name":"GOOG",
    "shares":100,
    "price": 490.10
}

# To access members of a dictionary, use the key-indexing operator
print stock["name"]
print stock["shares"]* stock["price"]

# Insert or modify objects
stock["name"] = "AB"
stock["date"] = "September 5, 2019"

print stock

# Strings are most common type of keys, you can use python objects including numbers, tuples. Some objects like lists and dictionaries
# cannot be used a keys because their content can change

# An empty dictionary is created in one of two ways
prices = {} # an empty dict
prices = dict() # an empty dict

# Dictionary membership is tested with the 'in' operator

if "name" in stock:
    print stock["name"]
else:
    print "not found"

print stock.get("name",0.0)

# To obtain a list of dictionary keys, convert a dictionary to a list
syms = list(stock) # syms = ['date', 'price', 'name', 'shares']
print syms

# Use del statement to remove an element of a dictionary
del stock["name"]
print stock

# Dictionaries are probably the most finely tuned data type in the python interpreter