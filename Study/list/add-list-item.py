# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "bananna", "chery"]
thislist.append("orange")
print(thislist) # ['apple', 'bananna', 'chery', 'orange']


# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:
thislist = ["apple", "bananna", "chery"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'bananna', 'chery']

# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "bananna", "chery"]
tropical = ["mango", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'bananna', 'chery', 'mango', 'papaya']

# Add Any Iterable
# The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "bananna", "chery"]
thistuple = ("orange", "mango")
thislist.extend(thistuple)
print(thislist) # ['apple', 'bananna', 'chery', 'orange', 'mango']