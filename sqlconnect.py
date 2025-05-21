import mysql.connector as connect
db = connect.connect(host="localhost",user="root",password="root",database="rrs")
cursor = db.cursor()

#db.close() is written in the main.py file as we need to close the connection in the end
