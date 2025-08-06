# List Comprehension
# List comprehension offers a shorter syntax when you want to create a 
# new list based on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list, containing only the fruits 
# with the letter "a" in the name.

# Without list comprehension you will have to write a for 
# statement with a conditional test inside:
fruits = ["apple", "bananna", "orange", "cherry", "kiwi"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) # ['apple', 'bananna', 'orange']

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "bananna", "orange", "cherry", "kiwi"]

newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'bananna', 'orange']

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
fruits = ["apple", "bananna", "orange", "cherry", "kiwi"]

newlist = [x for x in fruits if x != "apple"]
print(newlist) # ['bananna', 'orange', 'cherry', 'kiwi']

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# with condition 
newlist = [x for x in range(10) if x <=5]
print(newlist) # [0, 1, 2, 3, 4, 5]

# Expression
# The expression is the current item in the iteration, but it is also the outcome,
#  which you can manipulate before it ends up like a list item in the new list:
fruits = ["apple", "bananna", "orange", "cherry", "kiwi"]
newlist = [x.upper() for x in fruits]
print(newlist) # ['APPLE', 'BANANNA', 'ORANGE', 'CHERRY', 'KIWI']

# Set all values in the new list to 'hello':
newlist = ["hello" for x in fruits]
print(newlist) # ['hello', 'hello', 'hello', 'hello', 'hello']
