import sqlite3
import pandas as pd
db = sqlite3.connect('student3.db')
print("database open sucessfully")
#db.execute('''create table student (sno number primary key,sname text(20),age number,total_marks number);''')
#print('table created succesfully')
db.execute(''' insert into student values(1,'yash',18,97);''')
db.execute(''' insert into student values(2,'ram',19,87);''')
db.execute(''' insert into student values(3,'jay',18,77);''')
db.execute(''' insert into student values(4,'yug',19,77);''')
db.execute(''' insert into student values(5,'vedant',18,87);''')
db.execute(''' insert into student values(6,'krish',17,92);''')
print("data inserted succesfully")
df = pd.read_sql_query("SELECT * FROM student", db)
print(df)
top = df.head(3)
print(top)
dc=df[df['age']>=18]
print(dc)
print('\n')
result = df.loc[df['sno'] == 5,'age']
print(result)
result2= df[df['sno'] == 5].index[0]
result3= df.iloc[result2,2]
print(result3)








