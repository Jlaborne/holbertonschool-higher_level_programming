#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306)
    
    # Create a cursor object
    c = db.cursor()
    
    # Execute the query
    c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    
    # Fetch all the rows
    states = c.fetchall()
    
    # Print the results
    for state in states:
        print(state)
    
    # Close the cursor and connection
    c.close()
    db.close()
