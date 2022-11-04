# Reversing the contents of a string
print("...A program to reverse the contents of a string...")
# Declare the string
while True: # Only accept strings
    try:
        text = str(input("Please enter the text you wish to reverse: "))
    except:
        print("Please use texts only: ")
    break
# Get the string length
text_length = len(text)
print("Your text was '{}', and it's reversed format is: {}".format(text, text[text_length::-1]))


