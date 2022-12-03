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

else: # For strong passwords
    # Have a list of symbols, numbers, and letters
    # Remember, a strong password ought to have both upper and lower case letters
    # Symbols list
    symbols = [
        "~", "!", "@", "$", "%", "^", "&", ",", "*", "(", ")", "–", "_", 
        "=", "+", "[", "]", "{", "}", "{", "}", "|", ";", ":", "‘", "“", 
        ".", "/", "<", ">", "<", ">", "?"
    ]
    random_symbols_1 = random.sample(symbols, 2) # get two random symbols
    random_symbols_2 = random.sample(symbols, 2) # get another two random symbols
    # Join the symbols
    random_symbols_joined_1 = "".join(random_symbols_1)
    random_symbols_joined_2 = "".join(random_symbols_2)
    # Numbers list
    numbers = list(str(random.randrange(1000, 9999))) # generate random 4 digits number
    random_numbers_1 = random.sample(numbers, 2) # get two digits
    random_numbers_2 = random.sample(numbers, 2) # get another two digits
    # Join the numbers
    random_numbers_joined_1 = "".join(random_numbers_1)
    random_numbers_joined_2 = "".join(random_numbers_2)
    # letters
    letters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
    # Generate random letters in both upper and lower cases
    password_letters_1 = random.sample(letters, 4) # get two letters
    password_letters_2 = random.sample(letters, 4) # get another two letters
    # Join the letters
    password_letters_joined_1 = "".join(password_letters_1)
    password_letters_joined_2 = "".join(password_letters_2)
    # Now join these to form a strong password
    print("Your password is: ")
    print(
        "{}{}{}{}{}".
        format(password_letters_joined_1, random_symbols_joined_1, random_numbers_joined_1,
         password_letters_joined_2, random_numbers_joined_1, random_symbols_joined_2)
         )
    
    




