# Copy a Dictionary
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# nother way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}