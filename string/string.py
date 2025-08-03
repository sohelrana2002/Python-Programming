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