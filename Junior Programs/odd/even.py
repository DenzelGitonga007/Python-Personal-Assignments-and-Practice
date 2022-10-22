# Evaluate if a number is even or odd
number = int(input("Enter any number: "))
if number % 2 != 0:
    print("{} is an odd number".format(number))
else:
    print("{} is an even number".format(number))