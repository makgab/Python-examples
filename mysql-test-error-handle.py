#!/usr/bin/python3

import MySQLdb as sql
import time

print("Starting...")

mydb = None

while True:
    try:
        # conncetion:
        if (mydb):
            print("MySQL connection is OK.")
        else:
            print("MySQL connection has problem! Reconnect...")
            mydb = sql.connect(
                host="localhost",
                user="user",
                passwd="passwd",
                database="database_name",
                connect_timeout=10
            )

        print(mydb)

        # SELECT SQL
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM data;")
        for x in mycursor:
            print(x)

    except (Exception) as e:
        print("Error in MySQL connection:")
        print(e)

    finally:
        print("End.")
        time.sleep( 5 )
# end while
