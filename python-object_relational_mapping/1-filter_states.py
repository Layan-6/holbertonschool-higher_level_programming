#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
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
    
    # Execute SQL query to select states where name starts with 'N'
    # Use LIKE 'N%' to match names starting with N
    # Use BINARY to make it case-sensitive (N vs n)
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    # Fetch all rows
    states = cursor.fetchall()
    
    # Print each state
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
