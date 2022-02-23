from connection import mydb

mycursor = mydb.cursor()

#mycursor.execute("create database pythonsql")

mycursor.execute("show databases")

for x in mycursor:
    print(x)


