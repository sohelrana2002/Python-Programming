# The built-in range() function returns an immutable sequence of numbers, 
# commonly used for looping a specific number of times.
# This set of numbers has its own data type called range

# Creating ranges
# The range() function can be called with 1, 2, or 3 arguments, using this syntax:
# range(start, stop, step)

x = range(10)

print(x)

#convert to list to display the content of x:
print(list(x))

# Call range() With Two Arguments
# If the range function is called with two arguments, the first argument 
# represents the start value, and the second argument represents the stop value.

# range(3, 10) returns a sequence of each number from 3 to 9:

x = range(3, 10)

print(x)

#convert to list to display the content of x:
print(list(x))

# Call range() With Three Arguments
# If the range function is called with three arguments, the third argument
#  represents the step value.

x = range(3, 10, 2)

print(x)

#convert to list to display the content of x:
print(list(x))

for x in range(10):
  print(x) 


r = range(0, 10, 2)
print(list(r))
print(len(r))


