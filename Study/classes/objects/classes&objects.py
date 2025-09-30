class myClass:
    x = 5

obj1 = myClass()
print(obj1.x)
# output 5

# The __init__() Method
# The examples above are classes and objects in their simplest form, 
# and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() method.

# All classes have a method called __init__(), which is always executed when 
# the class is being initiated.

# Use the __init__() method to assign values to object properties, or 
# other operations that are necessary to do when the object is being created:

class Person:
    def __init__(self, name, age): #double underscore
        self.name = name
        self.age = age

p1 = Person("Sohel", 26)

print(p1.name)
print(p1.age)
# output Sohel 26
# Note: The __init__() method is called automatically every time the class is being used to create a new object.

# The __str__() Method
# The __str__() method controls what should be returned when the class object is 
# represented as a string.

# If the __str__() method is not set, the string representation of the object is returned:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} and {self.age}"

p1 = Person("Sohel", 26)
print(p1)
# output Sohel and 26

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myFunc(self):
        print("Hello my name is: " + self.name)

p1 = Person("Sohel", 26)
p1.myFunc()
# output Hello my name is: Sohel

# The self Parameter
# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:


# Modify Object Properties
# You can modify properties on objects like this:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myFunc(self):
        print("Hello my name is: " + self.name)

p1 = Person("Sohel", 26)
p1.myFunc()

p1.age = 40
print(p1.age)
# output 40

# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("Sohel", 26)

# del p1.age

# print(p1.age)
# error: AttributeError: 'Person' object has no attribute 'age'

# delete object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Sohel", 26)

del p1

print(p1)
# error : NameError: name 'p1' is not defined
