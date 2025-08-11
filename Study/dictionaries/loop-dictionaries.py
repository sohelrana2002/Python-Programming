# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary,
#  but there are methods to return the values as well.
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}

for x in thisdict:
    print(x)

# output brand
# model
# year
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}

for x in thisdict:
    print(thisdict[x])
# output Ford
# Mustang
# 1964

# You can also use the values() method to return values of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}

for x in thisdict.values():
    print(x)

# output 
# Ford
# Mustang
# 1964

# You can use the keys() method to return the keys of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}

for x in thisdict.keys():
    print(x)

# output 
# brand
# model
# year

# Loop through both keys and values, by using the items() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}

for x, y in thisdict.items():
    print(x, y)

# brand Ford
# model Mustang
# year 1964