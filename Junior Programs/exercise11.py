'''*Day 11 of 21:* A simple cipher
- Given a one-word message, take every letter in the word and 
replace it with its place in the alphabet.
- For each number in the created list, multiply it by 3 and subtract 5. 
Repeat this process n times.
Implement this by creating two functions, encrypt() and decrypt().
    encrypt() --> takes in the word and the key(n) as input and then outputs the encryped
    Output: word encrypted with The Cipher
Examples:
n = 2: "abc" >> [1, 2, 3] >> [-2, 1, 4] >> [-11, -2, 7]
n = 3: "hi" >> [151, 178]

    decrypt() --> Takes in the encrypted_word - A word that got encrypted with 
    The Cipher and n - the key
    Output: encrypted_word, decrypted
Examples:
n = 2: [16, 25, 34] >> [7, 10, 13] >> "def"
n = 5: [1339, 610, 2311, 2311, 3040] >> "hello" '''
word = 'hello' #our one word message
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = 5
crypt = [] #we will append our encrypt output in this list
#encrypt function- will encrypt our one word message i.e 'hello'
#encrypt function will take two variables: word and n- no of times we will repeat the encrypt process
def encrypt (string, n): 
    for letter in string: #for every letter in 'hello' e.g h
        for index, value in enumerate(alphabet,1): #will enumerage alphabet such that a = index 1, b= index 2, c=index3 ...h = index8
#the next part is to take the number representative of our word 'hello', thats where enumerate and if statement comes in
            if letter == value: #if letter in 'hello' and 'value' in alphabet match eg h ==h, we take its number representative that is index, used later in the code
#the while loop and counter is used to keep track of the number of times we run the encryption process
                counter = 0 #keeps count of the number of times we run the while loop, starts at 0
                while (counter<n): #the while loop will run n times. if n = 2, while loop will run twice then break, *remember counter keeps track of number of times we run the loop
                    index = index*3-5 #take index (number representative) the letter eg for h is 8 and multiply 8 by 3 subtract 5
                    counter =counter +1 #every time the while loop runs counter increases by 1
                crypt.append(index) #append the resulting number code in the crypt list (encryption)
    return (crypt) #return encryption
print (encrypt(word,number)) #call function

#decrypt function, does the complete opposite of encrypt function
#it will take in crypt-the encryption and N- the number of times we run the encryption process
def decrypt(crypt,n):
    sol = [] # we will append our output in this list
    for number in crypt: #for every number in our encrypted list
        counter = 0 #keeps count of the number of times we run the while loop, starts at 0
        while (counter<n): #the while loop will run n times. if n = 2, while loop will run twice then break, *remember counter keeps track of number of times we run the loop
            number = int((number+5)/3) #the reverse formula, the result will be the number representation of the letter
            counter =counter +1 #every time the while loop runs, counter increases by 1
#the next part is to get the letter which the number represents. We use enumerate function
#enumerate will assign all the letters of the alphabet a number/ index 
        for index, value in enumerate(alphabet,1):
#if function - if number from formula e.g.8 matches with the index from the alphabet e.g 8, we take its corresponding letter i.e 8
            if index == number:
                sol.append(value) #we append the letter to sol
    originalword= ''.join(sol) #the join function puts the output as a single word e.g. transforms [h,e,l,l,o] to [hello] 
    return (originalword) #return the word i.e. hello
print (decrypt (crypt,number)) #call the function