import mysql.connector
from mysql.connector import Error, errorcode

try:
    # Connect to the database
    mydb = mysql.connector.connect(
        user="movies_user",
        password="popcorn",
        host="localhost",
        database="movies",
        raise_on_warnings=True
    )
    cursor = mydb.cursor()

    # Function to display films
    def show_films(cursor, title):
        query = """
            SELECT film_name, film_director, genre_name, studio_name
            FROM film
            JOIN genre ON film.genre_id = genre.genre_id
            JOIN studio ON film.studio_id = studio.studio_id
        """
        cursor.execute(query)
        films = cursor.fetchall()
        print("\n—{}—".format(title))
        for film in films:
            print("Film Name:", film[0])
            print("Director:", film[1])
            print("Genre Name ID:", film[2])
            print("Studio Name:", film[3])
            print()

    # Display films before changes
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new record for Titanic
    insert_query = """
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        SELECT 'Titanic', '1997', '195', 'James Cameron', studio.studio_id, genre.genre_id
        FROM studio
        JOIN genre ON genre.genre_name = 'Thriller'
        WHERE studio.studio_name = 'Fox Baja'
    """
    cursor.execute(insert_query)
    mydb.commit()

    # Display films after insertion
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update a record
    update_query = "UPDATE film SET genre_id = %s WHERE film_name = %s"
    update_data = (1, "Alien")  # Assuming the new genre_id for Horror is 1
    cursor.execute(update_query, update_data)
    mydb.commit()

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete a record
    delete_query = "DELETE FROM film WHERE film_name = %s"
    delete_data = ("Gladiator",)
    cursor.execute(delete_query, delete_data)
    mydb.commit()

    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except Error as e:
    print("Error:", e)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
