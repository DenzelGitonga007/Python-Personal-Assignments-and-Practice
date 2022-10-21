# printing asterisks based on an iteration
# setting the limit for the stars
limit = int(input("How many stars do you wish to see? "))
for rows in range(0, limit): #assign the rows
    for columns in range(0, rows+1): #assign the columns to iterate (rows += 1)
        # print the stars
        print("* ", end=" ")
    # Print each on a new row
    print("\r")

#Trying a 180 degrees turn
print(" ")
print("...180 degrees turn...")
print(" ")
row_limit = limit
column_limit = limit
for row_num in range(0, row_limit+1): #assigning the rows
    for column_num in range(column_limit-row_num, 0, -1):
        # Print the stars
        print("* ",end=" ")
    # Print each on new rows
    print("\r")

