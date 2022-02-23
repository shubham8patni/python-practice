from connection import mydb

mycursor = mydb.cursor()

# alter 1 at a time
mycursor.execute("create table employee (id INT auto_increment primary key, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("create table department (name VARCHAR(255), salary INT(255))")
mycursor.execute("alter table department add column id INT Auto_increment primary key ")
mycursor.execute("alter table department add column employee_id INT not null default 0")
mycursor.execute("alter table department add foreign key (employee_id) references employee(id)")

mycursor.execute("show tables")

for x in mycursor:
    print(x)