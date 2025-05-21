import mysql.connector as connect
db = connect.connect(host="localhost",user="root",password="root")
cursor = db.cursor()
cursor.execute("create database rrs;")
cursor.execute("use rrs;")
cursor.execute("create table user_bookings(username char(30),start_datetime char(100),end_datetime char(100),train_no int,pnr int,booking_status char(30),current_status char(30),class char(30),name varchar(30),age int,gender char(30),board char(30),destination char(30),status char(50),train_name char(30));")
cursor.execute("create table trains(train_no int primary key,train_name char(50),running_days char(200),coaches varchar(500));")