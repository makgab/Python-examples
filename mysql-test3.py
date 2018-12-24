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


print ("SELECT SQL...")

# SELECT SQL
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pythonDB.customers")
for x in mycursor:
  print(x)


# end
