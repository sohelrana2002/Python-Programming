print(10 >= 9) # output True
print(20 == 30) # output False
print(30 < 10) # output False

a = 30
b = 20

if a > b:
    print("a is greater then b")
else:
    print("b is greater then a")

print(bool("Hello")) # output True
print(bool(15)) # output True

print(bool("abc")) # output True
print(bool(123)) # output True
print(bool(["apple", "cherry", "banana"])) # output True

print(bool(False)) # output False
print(bool(None)) # output False
print(bool(0)) # output False
print(bool("")) # output False
print(bool(())) # output False
print(bool([])) # output False
print(bool({})) # output False

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 15
print(isinstance(x, int)) # output True