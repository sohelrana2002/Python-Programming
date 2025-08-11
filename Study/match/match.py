# The match statement is used to perform different actions based on different conditions.

# The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.
# Syntax 
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

# The example below uses the weekday number to print the weekday name:

day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# output Thursday

# Default Value
# Use the underscore character _ as the last case value 
# if you want a code block to execute when there are not other matches:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("This day is not exist!")

# output This day is not exist! 
# The value _ will always match, so it is important to place it as the last case 
# to make it behave as a default case.

# Combine Values
# Use the pipe character | as an or operator in the case evaluation 
# to check for more than one value match in one case:
day = 6

match day:
    case 1 | 2 | 3 | 4:
        print("Today is weekday")
    case 5 | 6:
        print("I love weekends")

# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 if month == 4:
        print("Week day in april")
    case 1 | 2 | 3 | 4 if month == 5:
        print("Week day in may")
    case _:
        print("No weekends")