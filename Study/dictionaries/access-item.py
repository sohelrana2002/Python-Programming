# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) # Mustang

# There is also a method called get() that will give you the same result:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")
print(x) # Mustang

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x) # dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any 
# changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) # dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
x = car.keys()
print(x)  # dict_keys(['brand', 'model', 'year', 'color'])

# Get Values
# The values() method will return a list of all the values in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x) # dict_values(['Ford', 'Mustang', 1964])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change dict_values(['Ford', 'Mustang', 2020])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x) #after the change dict_values(['Ford', 'Mustang', 1964, 'red'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"

print(x) #after the change dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("Yes! It is present!")