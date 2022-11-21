# Getting the factorial of numbers
# Method 1: Using if statements
print("...Get factorial of numbers...")
# Get user input
user_num = int(input("Enter the number to find factorial for: "))
# The number to multiply
multiply = 1
print("The values from 1 to {} are: ".format(user_num))
for values in range(1, user_num + 1):
    print(values)
    # To multiply the values
    multiply = multiply * values
print("The factorial is: ", multiply)

# Method 2: Math.factorial method
import math
# Get user input
user_num_2 = int(input("Enter another number: "))
print("{} factorial is: ".format(user_num_2), math.factorial(user_num_2))
