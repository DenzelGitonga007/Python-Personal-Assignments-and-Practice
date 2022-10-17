# Initializing strings and printing the first, middle,
# and last characters
string_one = input("Enter a name, any name: ")
string_two = input("Enter a second one: ")
print(string_one[0] + string_two[0] + 
        string_one[int(len(string_one)/2)] + string_two[int(len(string_two)/2)] + 
        string_one[-1] + string_two[-1]
    )


