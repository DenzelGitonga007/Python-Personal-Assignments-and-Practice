#A function to return the largest number in a list
print("...Get the largest number in a list...")
def largest_number(numbers):
    """Get the largest number in a list""" #help
    # Set the limit for the list
    # Take only numbers
    while True:
        try:
            limit = int(input("Please enter how many numbers do you wish to test: "))
            break
        except:
            print("Invalid input, system can only take numbers")
    print("Please key them in: ")
    for values in range(0, limit):
        # Take only numbers
        while True:
            try:
                values = int(input())
                # Append the values into the numbers list
                numbers.append(values)
                break
            except:
                print("Please enter numbers only: ")
    print("The numbers you entered are: {}".format(numbers))
    print("Arranged in ascending order: {}".format(sorted(numbers)))
    results = print("The largest of these is: {}".format(max(numbers)))
    return results
# Initialize the list
numbers = []
# Call the function
largest_number(numbers)
