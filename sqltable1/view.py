from django.http import HttpResponse
from django.shortcuts import render,redirect
from connection import connections


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
    mydb = connections.conn

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
    return render(request, "sql_table.html", {'list1': list1})

    # mydb.commit()
    # mydb.close()

    # return HttpResponse("success")


def search(request):
    name = request.GET['text1']
    # print(type(name))
    list1 = []
    # print(name)
    mydb = connections.conn

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
    # print(list1)
    new_data = []
    for x in list1:
        if name.upper() in x['name'].upper():
            new_data.append(x)

    return render(request, "sql_table.html", {'list1': new_data})

def append(request):
    list1 = []
    name = request.GET['text1']
    mobile = request.GET['text3']
    age = request.GET['text2']
    gender = request.GET['text4']

    mydb = connections.conn
    cr = mydb.cursor()
    cr.execute(
        "insert into student (name,age,mobile,gender) values ('" + name + "','" + age + "','" + mobile + "','" + gender + "')")
    mydb.commit()
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

    # return render(request, 'sql_table.html', {'list1': list1})
    return redirect(show)



def delete(request):
    list1 = []
    id = request.GET['bt2']
    # print(type(id))
    mydb = connections.conn
    cr = mydb.cursor()

    cr.execute("delete from student where id='" + id + "'")

    mydb.commit()

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

    return render(request, 'sql_table.html', {'list1': list1})


def edit(request):
    list1 = []
    id = request.GET['bt3']
    mydb = connections.conn
    cr = mydb.cursor()

    cr.execute("select * from student where id = '"+id+"'")
    name_list = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[1]] = x[1]
        dict1[name_list[2]] = x[2]
        dict1[name_list[3]] = x[3]
        dict1[name_list[4]] = x[4]
        list1.append(dict1)
    return render(request,"edit_page.html",{'list1':list1})

def update(request):
    list1 = []
    id = request.GET['sp1']
    name = request.GET['text1']
    age = request.GET['text2']
    mobile = request.GET['text3']
    gender = request.GET['text4']

    mydb = connections.conn
    cr = mydb.cursor()

    cr.execute("update student set name='"+name+"', age='"+age+"', mobile='"+mobile+"', gender='"+gender+"' where id = '"+id+"'")
    mydb.commit()
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
    return render(request,"sql_table.html",{'list1':list1})


