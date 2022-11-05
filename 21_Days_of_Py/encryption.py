# *Day 11 of 21:* A simple cipher
# - Given a one-word message, take every letter in the word and replace it with its place in the alphabet.
# - For each number in the creaed list, multiply it by 3 and subtract 5. Repeat this process n times.
# Implement this by creating two functions, encrypt() and decrypt().
#     encrypt() --> takes in the word and the key(n) as input and then outputs the encryped
#     Output: word encrypted with The Cipher
# Examples:
# n = 2: "abc" >> [1, 2, 3] >> [-2, 1, 4] >> [-11, -2, 7]
# n = 3: "hi" >> [151, 178]

#     decrypt() --> Takes in the encrypted_word - A word that got encrypted with The Cipher and n - the key
#     Output: encrypted_word, decrypted
# Examples:
# n = 2: [16, 25, 34] >> [7, 10, 13] >> "def"
# n = 5: [1339, 610, 2311, 2311, 3040] >> "hello"

# Prompt the user to enter the word
word = str(input("Please enter the word you wish to encrypt: "))
# How many times to run the encryption
n = int(input("How many times do you wish to run the encryption on the word: "))
print("Your word is '{}'".format(word))
# Declaring the alphabets list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
# Declare the list for the encryped word
encrypted_word = []
# Create the encrypt function
def encrypt (word, n):
    # Access the word letters
    for letter in word:
        # Access the alphabets with their index
        for index, value in enumerate(alphabet,1):
            if letter == value:
                # Setting how many times to encrypt, based on n
                encryption_count = 0
                while (encryption_count<n):
                    # Multiply the index by 3 and minus 5
                    index = (index * 3)-5
                    encryption_count += 1
                    # Append these index to the encrypted_word
                    encrypted_word.append(index)
    return ("It's encryption format is: " + str(encrypted_word))
# Call the function
print(encrypt(word, n))