# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "bananna", "orange"]
thislist.remove("bananna")
print(thislist) # ['apple', 'orange']

# he pop() method removes the specified index.
thislist = ["apple", "bananna", "orange"]
thislist.pop(1)
print(thislist) # ['apple', 'orange']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "bananna", "orange"]
thislist.pop()
print(thislist) # ['apple', 'bananna']

# The del keyword also removes the specified index:
thislist = ["apple", "bananna", "orange"]
del thislist[0]
print(thislist) # ['bananna', 'orange']

# The del keyword can also delete the list completely.
thislist = ["apple", "bananna", "orange"]
del thislist
# print(thislist)
#this will cause an error because you have succsesfully deleted "thislist".

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "bananna", "orange"]
thislist.clear()
print(thislist) # []