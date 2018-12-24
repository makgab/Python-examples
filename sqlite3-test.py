# sqlite3

import sqlite3 as lite



con = lite.connect('homerseklet.db')
"""
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO adatok VALUES(?,?)",('2018-10-20 14:12:15','25°C'))
    con.commit()
"""

mycursor = con.cursor()

# 1
mycursor.execute("SELECT * FROM adatok;")
res = mycursor.fetchall()
for row in res:
    print(row)

# 2
for row in mycursor.execute('SELECT * FROM adatok;'):
    print(row)


con.close()
# end
