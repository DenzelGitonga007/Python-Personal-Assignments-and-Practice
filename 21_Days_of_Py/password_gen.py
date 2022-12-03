# Write a password generator in Python.
# Be creative with how you generate passwords:
# - Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# - The passwords should be random, generating a new password every time the user asks for a new password.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# Start
# print("...Password generator...")
# # Ask the user how strong they want their password to be
# # Also, only accept string values
while True:
    try:
        level = (input("How do you wish your password to be: weak or strong? "))
        print("You entered: ", level)
        if not level.isalpha() and level != "weak" or level != "strong":
            print("Please enter texts only, either strong or weak: ")
        else:
            break
    except:
        pass
print("For a {} password".format(level))
# For weak password



