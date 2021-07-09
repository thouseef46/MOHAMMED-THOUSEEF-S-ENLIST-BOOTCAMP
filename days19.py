import mysql.connector



import xlrd
import pandas as pd





mydata = mysql.connector.connect(host="localhost",user="root",passwd="MOHAMMED123#",database="sata")




mydb = mydata.cursor()
mydb.execute("create table id(stdid int primary key,name varchar(30),section char(10))")





loc =("C:\\Users\\ELCOT\\OneDrive\\Desktop\\days19.xlsx")
l =list()






a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,5):
    
    l.append(tuple(sheet.row_values(i)))


    





q = "insert into id(stdid,name,section)values(%s,%s,%s)"
mydata.close()    


# In[58]:
