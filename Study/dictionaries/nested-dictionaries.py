# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1": {
        "name": "Rashed",
        "age": 24
    },
    "child2": {
        "name": "Nur",
        "age": 23
    },
    "child3": {
        "name": "Sakib", 
        "age": 25
    }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, 
# starting with the outer dictionary:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child3"]["name"]) # Linus

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    # print(obj)

    for y in obj:
        print(y + ":", obj[y])

# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011
