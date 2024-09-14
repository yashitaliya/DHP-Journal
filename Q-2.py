import sqlite3
import pandas as pd
db=sqlite3.connect('employee.db')
#db.execute('''create table Employee(eno number primary key,ename text(20),designation text(10),basic number,da number,gross_salary number);''')
#print("table created")
db.execute(''' insert into Employee values(1,'yash','HR',35000,4200,39200);''')
db.execute(''' insert into Employee values(2,'ram','Finance',28500,4275,32775);''')
db.execute(''' insert into Employee values(3,'jay','Accountant',42000,3360,45360);''')
db.execute(''' insert into Employee values(4,'yug','CA',18750,2437.50,21187.50);''')
db.execute(''' insert into Employee values(5,'vedant','Doctor',50000,5000,55000);''')
print('data insert sucessfully')
df=pd.read_sql_query("select * from Employee",db)
print(df)
print('\n')
sort=df.sort_values(by = "gross_salary")
print(sort.tail(2))
print('\n')
sort1 = df[df['gross_salary']>25000]
print(sort1)
print('\n')
result = df.loc[df['eno']==4,'gross_salary']
print(result)
