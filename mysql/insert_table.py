from connection import mydb

mycursor = mydb.cursor()

#sql = "insert into employee (name, address) values (%s, %s)"
#val = ("jack", "meerut")

sql = "insert into department (name, salary, employee_id) values (%s, %s, %s)"
val = ("Shubham Patni", 65000, 1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")