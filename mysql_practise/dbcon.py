#We need to install this: python -m pip install mysql-connector-python

import mysql.connector
mydb = connect(
  host="103.187.31.18",
  user="root",
  port=5960,
  database="billing",
  password="dhaka123"
)

if mydb.is_connected:
        print("Mysql connected")
else:
    print("Mysql not connected")

mydb.close()