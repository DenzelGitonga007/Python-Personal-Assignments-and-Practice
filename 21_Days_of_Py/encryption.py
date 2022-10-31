# Encrypting words/texts
# This is by, capturing the word, assigning each letter in the word, 
# to its index in the alphabet

# Prompt the user to enter the word
word = str(input("Please enter the word you wish to encrypt: "))
print("Your word is '{}'".format(word))
# Declaring the alphabets list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
# Check if the letters exist in the alphabet
# for letters in word:
#     print(letters)
#     if letters in alphabet:
#         print("The letters are in the alphabet")
#     else:
#         print("Check the code")
# Get the index of each letter
for index, letters in enumerate(word, 1):
    # print(letters)
    print(index)