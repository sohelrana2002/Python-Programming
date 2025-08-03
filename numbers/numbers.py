# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print(z)


# Integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 2e3 # 2*10^3 = 2*1000 = 2000
y = 2E3 # 2*10^3 = 2*1000 = 2000
print(type(x))
print(x)
print(type(y))
print(y)

# Complex
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Convert from one type to another:
x = 1
y = 10.5
z = 5j

a = float(x)
b = int(y)
# c = int(z)
d = complex(y)

print(a)
print(b)
# print(c)
print(d)

print(type(a))
print(type(b))
# print(type(c))
print(type(d))

# we can't convert complex or imaginary part to int or float

# Random Number
# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers:
import random
x = random.randrange(1, 10)
print(x)
print(type(x))