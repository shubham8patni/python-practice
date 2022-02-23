from connection import mydb

mycursor = mydb.cursor()

sql = "select name from employee where id = (select employee_id from department order by salary desc limit 1)"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)