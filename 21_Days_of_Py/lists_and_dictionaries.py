# Creating a list of favorite movies, 
# and assigning them to different genres
# and display the output as key-value pair
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
print(genres)
    # for group, movie in genres.items():
    #     print("My favorite movie genre is {}. One such movie is {}".format(group, movie))
