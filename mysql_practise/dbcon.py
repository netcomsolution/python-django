#We need to install this: python -m pip install mysql-connector-python

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port=5960,
  database="billing",
  password="dhaka123"
)

if mydb.is_connected:
        print("Mysql connected")
else:
    print("Mysql not connected")
