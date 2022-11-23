# Couting the number of times a character repeats itself in a string
# Get the string input
test_string = input("Enter the text: ")
# Get the character to test
test_char = input("Which character do you wish to test: ")
# Variable to hold the count
count = test_string.count(test_char)
print("In the word {}, the letter {} repeats itself {} times".format(test_string, test_char, count))