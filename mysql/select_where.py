from connection import mydb

mycursor = mydb.cursor()

sql = "select name from employee where address = 'meerut'"
#sql = "select name from employee where address like '%gao%'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)