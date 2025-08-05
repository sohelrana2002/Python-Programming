# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

x = 5
y = "Sohel"

print(x)
print(y)

# reassign variable
x = 4 # x is of type int
x = "Sally" # x is of type string
print(x)

# Casting
# If you want to specify the data type of a variable, 
# this can be done with casting.

a = 5
x = int(a)
y = str(a)
z = float(a)

print(x)
print(y)
print(z)

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "SOHEL"

print(type(x))
print(type(y))

# Case-Sensitive
# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John


# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"


# Assign multuple value 
x, y, z = "Orange", "Green", "Yellow"

print(x)
print(y)
print(z)


# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. 
# This is called unpacking.

fruit = ["Apple", "Bananna", "Orange"]
x, y, z = fruit
# In the print() function, you output multiple variables, separated by a comma:
print(x, y, z)


# you can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)


# Global Variables
# Variables that are created outside of a function are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
x = "Awesome"

def myFun():
    print("Python is " + x)

myFun()

def myNewFun():
    x = "Joss"
    print("Python is " + x)

myNewFun()


# The global Keyword
# Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def newFun():
    global x
    x = "Fantastic"

newFun()
print("Python is " + x)