fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

# exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Using the range() function:
for x in range(6):
  print(x)

# The range() function defaults to 0 as a starting value, however it is possible
#  to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
# Example
# Using the start parameter:

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is 
# possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.

# Example
for x in [0, 1, 2]:
  pass