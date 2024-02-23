#Romany Manriquez
#Outhayvanh Somchaleun 
#Kristina Vasquez 

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    user= "bacchususer",
    password= "winewine",
    host= "localhost",
    database= "BACCHUS",
    raise_on_warnings= True
)

mycursor = mydb.cursor()

# Define a function to fetch and display data from a table
def display_table(table_name):
    print(f"Table: {table_name}")
    mycursor.execute(f"SELECT * FROM {table_name}")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    print()

# Display data from each table
tables = ["Owners", "Personnel", "Employees", "Grapes", "Suppliers", "Distributors", "Wines", "Production"]
for table in tables:
    display_table(table)

# Close the connection
mydb.close()
