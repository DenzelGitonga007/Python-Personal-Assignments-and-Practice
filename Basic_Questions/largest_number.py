# Create a function that prints the largest number in a list
print("...Get the largest number amongst many...")
# Create the function
def largest_number(numbers):
    # The help
    """ Prints out the largest number in a list """
    # # Initialize the list
    # numbers = []
    # Set a limit for the list
    limit = int(input("Please enter how many numbers do you wish to test from? "))
    # Get input based on limit
    for values in range(0, limit):
        while True: # Only take numbers
            try:
                values = int(input())
                # Append the values onto the list
                numbers.append(values)
                break # Stops at limit
            except:
                print("That's an invalid input, please enter numbers only")
        
    # Get the largest value
    print("The values you entered are: {}".format(numbers))
    print("Arranged in ascending order: {}".format(sorted(numbers)))
    print("The largest amongst these is: {}".format(max(numbers)))
# Initialize the list
numbers = []
# Call the function
largest_number(numbers)
