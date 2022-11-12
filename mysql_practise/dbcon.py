#We need to install this: python -m pip install mysql-connector-python

import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  port=3306,
  database="",
  password="dhaka123"
)

if mydb.is_connected:
        print("Mysql connected")
else:
    print("Mysql not connected")

mydb.close()