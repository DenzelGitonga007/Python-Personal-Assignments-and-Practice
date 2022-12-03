# Write a password generator in Python.
# Be creative with how you generate passwords:
# - Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# - The passwords should be random, generating a new password every time the user asks for a new password.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# Start
import random # For the random selection
print("...Password generator...")
# Ask the user how strong they want their password to be
while True:
    try:
        level = (input("How do you wish your password to be: weak or strong? "))
        if not level.isalpha():
            raise ValueError # Handled by the except function
        if level != "weak" and level != "strong":
            print("Please select either strong or weak, you entered: ", level)
        else:
            break
    except:
        print("Oops! Sorry, only text values allowed, you entered: ", level)
print("For a {} password:".format(level))
# For weak password
if level == "weak":
    # Get the user's name to have a list to pick two names from
    name = []
    number_of_names = 3
    print("Enter any three names so that we can randomly select two of them, and generate a password from these names")
    print("Hint: Type the name and press enter to type the next...")
    for names in range(0, number_of_names):
        # Get the names now
        names = input("")
        # Append the names onto the name list
        name.append(names)
    random_name = random.sample(name, 2)
    print("From {}, we have selected {} and {}".format(name, random_name[0], random_name[1]))
    # Now join the random_name to form the password
    print("And your password is: ","".join(random_name))


else:
    print("Strong strong...")




