from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from sqlite3 import *


# conn = connect('db.sqlite3')
# query ="select * from auth_user"
# cr = conn.cursor()
# cr.execute(query)
# data = cr.fetchall()
# print(data)


def index(request):
    return HttpResponse("<h1>hello World</h1>")


def indexpage(request):
    # data ={"Name":'Ram', 'class':10}
    data = ['Ram', 10, 6280995201]
    # return render(request, 'index.html',data)
    return render(request, 'index.html', {'data': data})


def addPage(request):
    return render(request, "addPage.html")


def getData(request):   #post module
    # name = request.POST['Name']
    # Class = request.POST['class']
    # mobile = request.POST['mobile']
    # # img = request.FILES['img']
    # # print(img)
    # print(request.POST)
    # for i in request.POST:
    #     print(f"{i}->", request.POST[i])
    # return render(request, 'demo.html', {'data': request.POST})
    # return HttpResponse(f"Success {name},{Class},{mobile},{request.POST}")
    mydb = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='test1'
    )

    cr = mydb.cursor()

    # cursor.execute("CREATE DATABASE test1")

    # cursor.execute("SHOW TABLES")

    # for x in cursor:
    #     print(x)

    # cursor.execute("CREATE TABLE student( id INT ,name varchar(25))")
    # cursor.execute("SHOW TABLES")
    # for x in cursor:
    #     print(x)

    # cursor.execute("INSERT INTO student(id,name) VALUES(1,'yuvraj')")

    # cursor.execute("SELECT * FROM student")
    # cursor.execute("ALTER TABLE student ADD PRIMARY KEY (id)")

    # cursor.execute("ALTER TABLE student MODIFY name varchar(25) NOT NULL ")

    # for x in cursor:
    #     print(x)

    # cursor.execute("INSERT INTO student(name) VALUES('vmm')")

    # cursor.execute("ALTER TABLE student MODIFY id int AUTO_INCREMENT")
    # sql="INSERT INTO student(name) VALUES(%s)"
    # val = [('sonu'),('kunal'),('delhi'),('rahul')]
    # cursor.executemany(sql,val)

    # cursor.execute("ALTER TABLE student ADD COLUMN age INT(2) NOT NULL ")
    # cursor.execute("ALTER TABLE student DROP COLUMN age")

    #
    # cursor.execute("ALTER TABLE student MODIFY age int(2) NULL")
    # cursor.execute("INSERT INTO student(age) VALUES('21')")
    # cursor.execute("UPDATE student SET age='23' where id='1'")
    # cursor.execute("UPDATE student SET age='30' where id='2'")
    # cursor.execute("UPDATE student SET age='25' where id='3'")
    # cursor.execute("UPDATE student SET age='22' where id='4'")
    # cursor.execute("UPDATE student SET age='26' where id='5'")
    # cursor.execute("UPDATE student SET age='32' where id='6'")
    list1 = []
    cr.execute("select * from student")
    column_names = [i[0] for i in cr.description]
    print(column_names)
    result = cr.fetchall()
    for x in result:
        dict1 = {}
        dict1[column_names[0]] = x[0]
        dict1[column_names[1]] = x[1]
        dict1[column_names[2]] = x[2]
        list1.append(dict1)
    print(list1)
    mydb.commit()
    mydb.close()
    return render(request, "demo.html", {"list1": list1})




# import sqlite3
#
# conn = sqlite3.connect("db.sqlite3")
#
# print(conn)
# import pymysql
#
# mydb = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='test1'
# )
#
# cursor = mydb.cursor()
#
# # cursor.execute("CREATE DATABASE test1")
#
# # cursor.execute("SHOW TABLES")
#
# # for x in cursor:
# #     print(x)
#
# # cursor.execute("CREATE TABLE student( id INT ,name varchar(25))")
# # cursor.execute("SHOW TABLES")
# # for x in cursor:
# #     print(x)
#
# # cursor.execute("INSERT INTO student(id,name) VALUES(1,'yuvraj')")
#
# # cursor.execute("SELECT * FROM student")
# # cursor.execute("ALTER TABLE student ADD PRIMARY KEY (id)")
#
# # cursor.execute("ALTER TABLE student MODIFY name varchar(25) NOT NULL ")
#
# # for x in cursor:
# #     print(x)
#
# # cursor.execute("INSERT INTO student(name) VALUES('vmm')")
#
# # cursor.execute("ALTER TABLE student MODIFY id int AUTO_INCREMENT")
# # sql="INSERT INTO student(name) VALUES(%s)"
# # val = [('sonu'),('kunal'),('delhi'),('rahul')]
# # cursor.executemany(sql,val)
#
# # cursor.execute("ALTER TABLE student ADD COLUMN age INT(2) NOT NULL ")
# # cursor.execute("ALTER TABLE student DROP COLUMN age")
#
# #
# # cursor.execute("ALTER TABLE student MODIFY age int(2) NULL")
# # cursor.execute("INSERT INTO student(age) VALUES('21')")
# # cursor.execute("UPDATE student SET age='23' where id='1'")
# # cursor.execute("UPDATE student SET age='30' where id='2'")
# # cursor.execute("UPDATE student SET age='25' where id='3'")
# # cursor.execute("UPDATE student SET age='22' where id='4'")
# # cursor.execute("UPDATE student SET age='26' where id='5'")
# # cursor.execute("UPDATE student SET age='32' where id='6'")
# list1 = []
# d = {}
# cursor.execute("select * from student order by name")
# for x in cursor:
#     d['id']=x[0]
# list1.append(d)
# print(list1)
# mydb.commit()
# mydb.close()
# # return render(request, "demo.html", {"list": list})
