# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))
# output : 15

# Lambda functions can take any number of arguments:
x = lambda a, b : a * b 
print(x(5, 6))
# output 

x = lambda a, b, c : a + b + c
print(x(5, 6, 7))
# output 18

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument 
# will be multiplied with an unknown number:

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(10)
print(myDoubler(5))
# output 50

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(10)
myTripler = myFunc(11)

print(myDoubler(5))
print(myTripler(6))
# output 50 & 66