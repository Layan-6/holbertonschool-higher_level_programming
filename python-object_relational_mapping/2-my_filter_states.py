#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Create SQL query using format with user input
    # WARNING: This is vulnerable to SQL injection!
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    
    # Execute the SQL query
    cursor.execute(query)
    
    # Fetch all rows
    states = cursor.fetchall()
    
    # Print each state
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
