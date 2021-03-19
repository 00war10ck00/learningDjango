from connection import connections
from prettytable import PrettyTable

def addto():
    mydb = connections.conn
    cr = mydb.cursor()
    name = input("enter name")
    clas = input("enter class")
    mobile = input("enter mobile")
    college = input("enter college")

    cr.execute("insert into stu(name,class,mobile,college) values('"+name+"','"+clas+"','"+mobile+"','"+college+"')")
    print("\n Data Inserted Successfully")
    mydb.commit()
    # mydb.close()


def updateto():
    mydb = connections.conn
    cr = mydb.cursor()
    roll_no = int(input("enter Roll No"))
    # print(type(roll_no))
    # cr.execute(f"select * from stu where id = {roll_no} ")
    cr.execute("select * from stu where id = {} ".format(roll_no))
    for x in cr:
        print(x)
    name = input("enter name")
    clas = input("enter class")
    mobile = input("enter mobile")
    college = input("enter college")
    cr.execute("update stu set name='"+name+"', class='"+clas+"', mobile='"+mobile+"', college='"+college+"'")
    print("\n Data Updated Successfully")
    mydb.commit()
    # mydb.close()


def delete():
    roll_no = input("Enter Roll No to Delete")

    mydb = connections.conn
    cr = mydb.cursor()

    cr.execute("select * from stu where id = {}".format(roll_no))
    print("\n Data Deleted------- ")
    for x in cr:
        print(x)

    cr.execute("delete from stu where id = {}".format(roll_no))
    mydb.commit()
    # mydb.close()


def search():
    roll_no = input("Enter Roll No To Search")
    mydb = connections.conn
    cr = mydb.cursor()
    query ="select * from stu where id = {}".format(roll_no)
    cr.execute(query)
    # print("\n Record found:")
    result = cr.fetchall()
    if len(result)>0:
        print(result)
    else:
        print("Data Not Found!!!!")
    # for x in cr:
    #     print(x)

def view():
    mydb = connections.conn
    cr = mydb.cursor()

    cr.execute("select * from stu")
    name_list = [i[0] for i in cr.description]
    t = PrettyTable(name_list)
    result = cr.fetchall()
    if len(result) > 0:
        for row in result:
            t.add_row(row)
        print(t)
    else:
        print("Data Not Found!!!!")

    # mydb.close()

def stop():
    exit(0)
while True:
    print("Enter 1 to Add Data")
    print("Enter 2 to Update Data")
    print("Enter 3 to Delete Data")
    print("Enter 4 to Search")
    print("Enter 5 to View Data")
    print("Enter 6 to Exit")
    num = int(input("Enter Your Choice"))
    if num == 1:
        addto()
    elif num == 2:
        updateto()
    elif num == 3:
        delete()
    elif num == 4:
        search()
    elif num == 5:
        view()
    elif num == 6:
        stop()



