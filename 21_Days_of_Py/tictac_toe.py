#*15*
#TIC TAC TOE GAME
## PART ONE -- Draw the tic tac toe board
# - Create a 3x3 board (like in tic tac toe). Obviously, they come in many other sizes 
# (8x8 for chess, 19x19 for Go, and many more).
# - Ask the user what size game board they want to draw, 
# and draw it for them to the screen using Python’s print statement.

# Get the size of the board from the user
while True:
    try:
        # Accept only integer values
        size = int(input("Enter the size of the board you wish to use:"))
        # The value should not be less than zero
        try:
            if size <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Size cannot be less than zero or zero itself")
    except:
        print("Please enter a numerical value only")

    