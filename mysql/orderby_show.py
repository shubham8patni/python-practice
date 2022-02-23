from connection import mydb

mycursor = mydb.cursor()

sql = "select * from employee order by name"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)