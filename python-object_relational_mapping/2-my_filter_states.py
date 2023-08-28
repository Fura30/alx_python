#!/usr/bin/python3
import MySQLdb
import sys

# Get command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to MySQL server
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Execute the SQL query to select all states matching the given name
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (state_name,))

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
