# mysql demo

import mysql.connector


# conncetion:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mysql"
)
print(mydb)


# show DB:
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# Drop DB
# mycursor = mydb.cursor()
# mycursor.execute("DROP DATABASE pythonDB")

# Create DB
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pythonDB")

# Create Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE pythonDB.customers (name VARCHAR(255), address VARCHAR(255))")

# INSERT SQL
mycursor = mydb.cursor()
sql = "INSERT INTO pythonDB.customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# SELECT SQL
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pythonDB.customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


# end
