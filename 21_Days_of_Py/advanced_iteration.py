# Create a list with numbers, and repeat those numbers n-times, in a new list
# Initialize the list
list_1 = []
# Set the limit for the list
# Limit should only be a number
while True:
    try:
        limit = int(input("Please enter how many numbers do you wish to test with: "))
        break
    except:
        print("Please enter a value that is a number only")
# Provide inputs based on the limit
print("Key in the numbers below:")
for num in range(0, limit):
    # Only accept numbers
    while True:
        try:
            num = int(input())
            break
        except:
            print("Please enter values that are numbers only")
    # Append the inputs/num into the list_1
    list_1.append(num)
print("Your numbers are {}".format(sorted(list_1)))
# Enter how many times you wish to repeat the numbers onto the new list
repeat = int(input("How many times do you wish to repeat each of these numbers? "))
# Initialize the new list
list_2 = []
# Iterate over the list_1 elements
for values in list_1:
    for repeat_limit in range(repeat):
        list_2.append(values)
print("The list when repeated {} times is: {}".format(repeat, list_2))