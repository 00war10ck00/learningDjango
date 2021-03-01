from django.http import HttpResponse
from django.shortcuts import render
import pymysql


# cr.execute("drop table student")
# cr.execute("create table student(id INT , name varchar(25),age INT ,mobile INT ,gender CHAR(1))")
# cr.execute("alter table student modify column id int auto_increment")

# cr.execute("alter table student modify column mobile varchar(10)")
# cr.execute("insert into student(id,name,age,mobile,gender) values(1,'yuvraj',24,9888659456,'M'),(2,'vmm',22,9888576456,'F'),(3,'nipun',26,9888659896,'M'),(4,'yuvi',30,9343559456,'M')")
# sql = "insert into student (id,name,age,mobile,gender) values (%s,%s,%s,%s,%s)"
# val = [
#     (1, 'yuvraj', 24, 988659456, 'M'),
#     (2, 'vmm', 22, 98834521, 'F'),
#     (3, 'nipun', 26, 98961334, 'M'),
#     (4, 'yuvi', 30, 934314134, 'M')
# ]
#
# cr.executemany(sql, val)

def show(request):
    list1 = []
    mydb = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='test'
    )

    cr = mydb.cursor()

    cr.execute("select * from student")
    name_list = [i[0] for i in cr.description]

    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[1]] = x[1]
        dict1[name_list[2]] = x[2]
        dict1[name_list[3]] = x[3]
        dict1[name_list[4]] = x[4]
        list1.append(dict1)
    return render(request,"table_show.html", {'list1': list1})

    mydb.commit()
    mydb.close()

    # return HttpResponse("success")

def search(request):
    name = request.GET['text1']
    list1=[]
    # print(name)
    mydb = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='test'
    )

    cr = mydb.cursor()

    cr.execute("select * from student")
    name_list = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[1]] = x[1]
        dict1[name_list[2]] = x[2]
        dict1[name_list[3]] = x[3]
        dict1[name_list[4]] = x[4]
        list1.append(dict1)
    for x in list1:
        if name in x['name']:
            list1.append(x)

    return render(request, "table_show.html", {'list1': list1})

    mydb.commit()
    mydb.close()
