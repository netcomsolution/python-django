import mysql.connector 

cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  port=3306,
  database="practise",
  password="dhaka123"
)
#my_cursor = cnx.cursor(dictionary=True)
my_cursor = cnx.cursor()
query = my_cursor.execute("SELECT customerId,fullName FROM billing_customer_info") 
result = my_cursor.fetchall()

for row in result:
    #print(row['customerId'],row['fullName'])
    print(row)
    