# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Union
# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {'a', 1, 2, 3, 'c', 'b'}

# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) # {1, 2, 3, 'c', 'a', 'b'}

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) # {1, 2, 3, 'b', 'c', 'apple', 'a', 'cherry', 'John', 'bananas', 'Elena'}

# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) # {'apple', 1, 2, 3, 'cherry', 'John', 'b', 'c', 'a', 'Elena', 'bananas'}

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
set1 = {"a", "b", "c"}
thistuple = (1, 2, 3)

myset = set1.union(thistuple)
print(myset) # {'b', 1, 2, 3, 'c', 'a'}

# Note: The  | operator only allows you to join sets with sets,
#  and not with other data types like you can with the  union() method.

# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set1 = {"a", "b", "c", 3}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) # {'b', 1, 2, 3, 'c', 'a'}
# Note: Both union() and update() will exclude any duplicate items.

# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains
#  the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # {'apple'}

# You can use the & operator instead of 
# the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) # {'apple'}

# Note: The & operator only allows you to join sets with sets, 
# and not with other data types like you can with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1) # {'apple'}

# Difference
# The difference() method will return a new set that will contain only the items from 
# the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3) # {'banana', 'cherry'}

# You can use the - operator instead of the difference() method,
#  and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) # {'banana', 'cherry'}

# Note: The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.

# The difference_update() method will also keep the items from the first set 
# that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1) # {'cherry', 'banana'}

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # {'google', 'cherry', 'microsoft', 'banana'}

# You can use the ^ operator instead of the symmetric_difference() method, 
# and you will get the same result
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) # {'google', 'cherry', 'microsoft', 'banana'}

# Note: The ^ operator only allows you to join sets with sets, and not with other data types
#  like you can with the symmetric_difference() method.

# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print("symmetric_difference_update", set1) # {'microsoft', 'google', 'cherry', 'banana'}