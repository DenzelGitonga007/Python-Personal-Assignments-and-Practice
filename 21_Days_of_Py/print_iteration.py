# printing asterisks based on an iteration
# setting the limit for the stars
limit = int(input("How many stars do you wish to see? "))
for rows in range(0, limit): #assign the rows
    for columns in range(0, rows+1): #assign the columns to iterate (rows += 1)
        # print the stars
        print("* ", end="")
    # Print each on a new row
    print("\r")