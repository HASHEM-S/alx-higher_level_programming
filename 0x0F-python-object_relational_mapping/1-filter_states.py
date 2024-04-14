#!/usr/bin/python3

import sys
import MySQLdb

def list_states_with_N(username, password, database):
    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(host="localhost",
                                     user=username,
                                     passwd=password,
                                     db=database,
                                     port=3306)
        cursor = connection.cursor()

        # Execute SQL query
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_with_N(username, password, database)
