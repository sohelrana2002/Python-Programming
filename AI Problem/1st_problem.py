# Teach the machine about animals

animal = {
    "cat": {"fur", "tail", "bright eyes"},
    "bird": {"wings", "peck", "tail"},
    "fish": {"scale", "fins","gills", "tail"}
}

userInput = input("Enter animal detaills: ")

userInput_list = userInput.split(" ")
print(userInput_list)
userInput_set = set(userInput_list)
print(userInput_set)

if userInput_set.issubset(animal["cat"]):
    print("It is cat!")
elif userInput_set.issubset(animal["bird"]):
    print("It is bird!")
elif userInput_set.issubset(animal["fish"]):
    print("It is fish")
else:
    print("I don't knowledge about that!")