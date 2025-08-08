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