# Arithmetic Operators
x = 5
y = 3

print(x + y) # output 8
print(x - y) # output 2
print(x * y) # output 15
print(x / y) # output 1.6666666666666667
print(x % y) # output 2
print(x ** y) # output x^y = 5^3 = 5*5*5 = 125
print(x // y) # Floor division output 1

# Logical Operators
# Logical operators are used to combine conditional statements:

x = 5

print(x > 3 and x < 10) # output True
# returns True because 5 is greater than 3 AND 5 is less than 10

print(x > 3 or x < 4) # output True
# returns True because one of the conditions are true 
# (5 is greater than 3, but 5 is not less than 4)

# Reverse the result, returns False if the result is true
print(not(x > 3 and x < 10)) # output False
# returns False because not is used to reverse the result


# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y

# Membership Operators
# It is used to test if a sequence is presented in an object:
x = ["apple", "bananna"]
print("bananna" in x)
# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
print(6 & 3) # output 2


"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 3) # output 7

"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

# XOR
print(6 ^ 3) # output 5

"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

# NOT: Inverts all the bits
print(~3) # output -4

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""


# left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3 << 2) # output 12

"""
The << operator inserts the specified number of 0's (in this case 2) from 
the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

# right shift	: Shift right by pushing copies of the leftmost bit in from 
# the left, and let the rightmost bits fall off
print(8 >> 2) # output 2

"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""