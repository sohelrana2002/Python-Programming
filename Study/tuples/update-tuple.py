# Change Tuple Values
# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, 
# change the list, and convert the list back into a tuple.

thistuple = ("apple", "bananna", "orange")
y = list(thistuple)
y[1] = "mango"
thistuple = tuple(y)
print(thistuple) # ('apple', 'mango', 'orange')

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple,
#  you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "bananna", "orange")
y = list(thistuple)
y.append("mango")
thistuple = tuple(y)
print(thistuple) # ('apple', 'bananna', 'orange', 'mango')

# Create a new tuple with the value "orange", and add that tuple:

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, 
# but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "bananna", "orange")
y_list = list(thistuple)
y_list.remove("bananna")
thistuple = tuple(y_list)
print(thistuple) # ('apple', 'orange')

# The del keyword can delete the tuple completely:
thistuple = ("apple", "bananna", "orange")
# del thistuple
# print(thistuple) # #this will raise an error because the tuple no longer exists