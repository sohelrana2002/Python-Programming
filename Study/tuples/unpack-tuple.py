# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables.
#  This is called "unpacking":

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, red, blue) = fruits
print(green) # apple
print(red) # banana
print(blue) #  cherry

# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, blue, *red) = fruits

print(green) # apple
print(blue) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry