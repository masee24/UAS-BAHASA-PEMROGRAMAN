import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="UAS_Bahasapemrograman"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("aji", "purworejo")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
