import mysql.connector
from mysql.connector import Error, errorcode

# Connect to the database
db = mysql.connector.connect(
    user= "movies_user",
    password= "popcorn",
    host= "localhost",
    database= "movies",
    raise_on_warnings= True
)

cursor = db.cursor()

# Query 1: Select all fields for the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("Studio Table:")
for studio in studios:
    print(studio)

# Query 2: Select all fields for the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\nGenre Table:")
for genre in genres:
    print(genre)

# Query 3: Select movie names for movies with a run time of less than two hours
cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
short_movies = cursor.fetchall()
print("\nShort Movies (< 2 hours):")
for movie in short_movies:
    print(movie[0])

# Query 4: Get a list of film names and directors grouped by director
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director")
directors = cursor.fetchall()
print("\nMovies Grouped by Director:")
for director in directors:
    print("Director:", director[0])
    print("Movies:", director[1])





cursor.close()
db.close()
