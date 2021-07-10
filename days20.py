import mysql.connector
tho=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MOHAMMED123#",
    database="empl")
cur=tho.cursor()
sql=("INSERT INTO employee(firstname,id,salary)VALUES(%s,%s,%s)")
values=[("talha","101","20000"),
       ("sam","102","30000"),
       ("kim","103","25000"),
       ("rem","104","40000")]
cur.executemany(sql,values)
tho.comit()
cur.execute("SELECT MIN(salary),MIN(salary)FROM employee")
myresult=cur.fetchall()
for i in myresult:
    print(i)

cur.execute("SELECT COUNT(DISTINCT firstname)FROM employee")
result=cur.fetchall()
for i in  result:
    print(i)

cur.execute("SELECT DISTINCT SUBSTRING(firstname,1,3)FROM employee")
res=cur.fetchall()
for i in res:
    print(i)
