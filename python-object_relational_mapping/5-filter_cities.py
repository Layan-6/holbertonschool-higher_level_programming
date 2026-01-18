#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Remove extra quotes if present
    # This handles cases like '''Arizona''' or '"Arizona"'
    if (state_name.startswith("'") and state_name.endswith("'")) or \
       (state_name.startswith('"') and state_name.endswith('"')):
        state_name = state_name[1:-1]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query with JOIN to get cities of specific state
    # Using parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Extract city names and join them with comma
    city_names = []
    for city in cities:
        city_names.append(str(city[0]))
    
    result = ", ".join(city_names)

    # Print result
    print(result)

    # Close cursor and database connection
    cursor.close()
    db.close()
