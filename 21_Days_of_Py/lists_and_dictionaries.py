# Creating a list of favorite movies, 
# and assigning them to different genres
# and display the output as key-value pair
print("..........Shall we try to classify your favorite movies..........?")
movies = []
# set the limit of users' movies list
limit = int(input("How many movies do you have in mind? "))
# Prompt the user to enter them
print("Please enter them below: ")
# Iterating over the movies list provided, based on the limit
for elements in range(0, limit):
    elements = str(input()) #The movies entered
    # Append the elements onto the movies
    movies.append(elements)
print(movies)    
# Initialize the dictionary
genres = {}
# setting the keys
# Prompt the user to group them into respective genres
print("Try classifying them into their respective genres below: ")
for key in range(0, limit):
    key = str(input())
    genres[key] = movies
    genres.update(zip(genres, movies))
# Now the dictionary is compiled, with the genres and the movies
# Iterate the dictionary therefore, to display each movie with
# its respective genre
for elements in genres.keys():
    print(f'My favorite movie genre is {elements}. One such movie or series is {genres[elements]} ')
