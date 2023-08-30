#!/usr/bin/env python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state.
"""

import sys
import MySQLdb

def filter_cities_by_state(username, password, database, state_name):
    # Establish a connection to the MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)
    
    # Execute the query to retrieve cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    try:
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        city_names = [city[0] for city in cities]
        city_list = ", ".join(city_names)
        print(city_list)
    except MySQLdb.Error as e:
        print("Error executing the query:", e)
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities_by_state(username, password, database, state_name)
 