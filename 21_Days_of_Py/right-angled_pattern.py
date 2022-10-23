#Print stars like a mountain
row = int(input("Set the size of the pattern: ")) #Takes the rows measure
column = row
for row_stars in range(0, row): #iterate over the rows
    for column_stars in range(0, row_stars):
        # for the left_stars
        # for left_stars in range(column_stars, 0, -1):
        #     print("* ", end=" ")
        # column_stars += 1;
        print("* ", end=" ")
    print("\r") #print on a new row