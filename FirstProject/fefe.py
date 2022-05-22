import sqlite3 
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
i = [("Peny", "Gog", 1970), ("Robert", "Mak", 1960), ("Pedro", "Sanches", 1111)]
# cursor.execute('''CREATE TABLE IF NOT EXISTS Shows(Title TEXT, Director TEXT, Year INT)''')

# cursor.execute('INSERT INTO Shows VALUES ("George", "Wolf", 1970)')
cursor.executemany('INSERT INTO Shows VALUES (?, ?, ?)', i)
cursor.execute('SELECT 1 FROM Shows')
print(cursor.fetchone())
data = cursor.fetchall()
print(type(data))
# print(cursor.fetchall())

connection.commit()
connection.close()
