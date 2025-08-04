# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't 
# match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes or Or three single quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(a)

# Strings are Arrays
a = "Hello!"
print(a[1])
print(len(a)) # 6 length of string

# Looping Through a String
a = "Apple"
for x in a:
    print(x)

# Check String 
name = "SOHEL RANA"
check  = "EL" in name
check2  = "Na" in name
print(check) # True
print(check2) # False

# It's provide true or false answer

# Use it in an if statement:
name = "MD: SOHEL RANA"

if "RANA" in name :
    print("Yes, Rana is present")
else:
    print("Not present")

# Check if NOT
name = "Fahim Rahman"

check = "Rahman" not in name
print(check) # False

# Get the characters from position 2 to position 5 (5 not included):
a = "Hello, World!"
print(a[2:5]) # output llo

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
a = "Hello, World!"
print(a[:5]) # output Hello

# Slice To the End
# By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:]) # output llo, World!

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2]) #output orl

# Modify Strings
# The lower() method returns the string in lower case:
name = "Sohel Rana"
print(name.lower()) # output sohel rana

# The upper() method returns the string in upper case:
print(name.upper()) # output SOHEL RANA

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, 
# and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
name = "   Sohel   Rana    "
print(name.strip()) # output Sohel   Rana

# Replace String
# The replace() method replaces a string with another string:
print(name.replace("S", "H")) # output Hohel   Rana

# Split String
# The split() method returns a list where the text between the specified 
# separator becomes the list items.
name = "Sohel Rana"
print(name.split(" ")) #output ['Sohel', 'Rana']

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
# age = 26
# name = "My name is Sohel and I'm " + age
# print(name)
# This will produce an error:

# But we can combine strings and numbers by using f-strings or the format() method!

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders 
# for variables and other operations.

age = 26
name = f"My name is Sohel and I'm {age} years old"
print(name)

# Display the price with 2 decimals:
price = 59
txt = f"This product is {price:.2f} dolar"
print(txt)

txt = f"The price is {10 * 59} dollars"
print(txt)

# Escape Character
txt = "We are the so-called \"Vikings\" from the north." 
print(txt)

# String Methods
name = "sohel rana"

# Converts the first character to upper case
print(name.capitalize()) # output Sohel rana

# Converts string into lower case
print(name.casefold()) # output sohel rana

# Returns a centered string
print(name.center(30)) # output sohel rana 30 px in left

# Returns the number of times a specified value occurs in a string
print(name.count("a")) # output 2

# Searches the string for a specified value and returns the position of where it was found
print(name.find("a")) # output  7(indexed num.)

# Returns True if all characters in the string are lower case
print(name.islower()) # output True

# Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
result = "$".join(myTuple)
print(result) # output John$Peter$Vicky

# title() Method
# Make the first letter in each word upper case:
txt = "Welcome to my world"
print(txt.title()) # output Welcome To My World


