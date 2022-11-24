# Arpasland has surrounded by attackers. A truck enters the city. 
# The driver claims the load is food and medicine from Iranians. 
# Ali is one of the soldiers in Arpasland. He doubts about the truck, 
# maybe it's from the siege. He knows that 
# a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. 
# Determine if the tag of the truck is valid or not.
# We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

# Get the string input from the user
tag = input()
# print(tag.split())
# Split the tag into elements in a list
tag_list = list(tag)
# print("The values of the tag are: ", tag_list)
# The vowels allowed
vowels = ["A", "E", "I", "O", "U", "Y"]
# Checking for the two consecutive numbers summation
# Add index of concecutive numbers
summation_1 = int(tag_list[0]) + int(tag_list[1]) 
summation_2 = int(tag_list[3]) + int(tag_list[4])
summation_3 = int(tag_list[4]) + int(tag_list[5])
summation_4 = int(tag_list[7]) + int(tag_list[8]) 
# The output
Invalid = "invalid"
if summation_1 % 2 == 0 and str(tag_list[2]) not in vowels:
    # Check that the numbers are consecutive only
    # if int(tag_list[1]) - int(tag_list[0]) == 1:
    print("valid")
elif summation_2 % 2 == 0 and str(tag_list[2]) not in vowels:
    print("valid")
elif summation_3 % 2 == 0 and str(tag_list[2]) not in vowels:
    print(Invalid)
elif summation_4 % 2 == 0 and str(tag_list[2]) not in vowels:
    print("valid")
else:
    print(Invalid)


