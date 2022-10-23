# Return the largest number in a list
# Declare an empty list
numbers = []
# Set the limit for the list
limit = int(input("How many numbers do you wish to test? "))
# Let the user input these numbers, upto the limit
for num in range(0, limit):
    num = int(input())
    # Append the inputs, nums to the numbers list
    numbers.append(num)
# Show the numbers list
print("The numbers you entered are {}".format(numbers))
print("In ascending order: {}".format(sorted(numbers))) #sorts the numbers in ascending order
# Checking for the largest number in the numbers list
# Ways to get the largest number
print("The largest number is:", max(numbers))

numbers.sort()
print("The largest number is: {}".format(numbers[-1]))
