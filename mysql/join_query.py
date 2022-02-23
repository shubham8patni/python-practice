import imp
from connection import mydb

mycursor = mydb.cursor()

sql = "select * from employee e inner join department d on e.id=d.employee_id"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)