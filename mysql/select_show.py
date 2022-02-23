from connection import mydb

mycursor = mydb.cursor()

#sql = "select * from employee"

mycursor.execute("select * from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


