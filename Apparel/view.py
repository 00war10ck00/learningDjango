from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from sqlite3 import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import date
data1 = []
count = 0


def connection():
    conn = connect('db.sqlite3')
    return conn


def index(request):
    data = []
    data1 = []
    count = -1
    mydb = connection()
    cr = mydb.cursor()
    # query = "alter table my_site_category add column photo varchar(255)"
    # cr.execute(query)
    # query = "insert into my_site_product(name,price,discount,photo, category_id) values('Fashionablel womens-original-trucker', '$221.00','$199.00','/media/products/product21.jpg', 2 )"
    # # , ('women', 'women clothing', '/media/categories/category1.jpg'), (
    # # 'shoes', 'shoes collection', '/media/categories/category1.jpg'), (
    # #   'kids', 'kids collection', '/media/categories/category1.jpg')
    # cr.execute(query)
    # mydb.commit()
    query = "select * from my_site_category"
    cr.execute(query)
    name_fields = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_fields[0]] = x[0]
        dict1[name_fields[1]] = x[1]
        dict1[name_fields[2]] = x[2]
        dict1[name_fields[3]] = x[3]
        data.append(dict1)

    query = "select * from my_site_product"
    cr.execute(query)
    name_fields = [i[0] for i in cr.description]
    for x in cr:
        count += 1
        dict1 = {}
        dict1[name_fields[0]] = x[0]
        dict1[name_fields[1]] = x[1]
        dict1[name_fields[2]] = x[2]
        dict1[name_fields[3]] = x[3]
        dict1[name_fields[4]] = x[4]
        dict1[name_fields[5]] = x[5]
        dict1['count'] = count
        data1.append(dict1)
    return render(request, 'index.html', {'data': data, 'data1': data1})


def product(request):
    data = []
    id = request.GET['id']
    mydb = connection()
    cr = mydb.cursor()
    query = "select * from my_site_product where id = '"+id+"'"
    cr.execute(query)
    name_list = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[1]] = x[1]
        dict1[name_list[2]] = x[2]
        dict1[name_list[3]] = x[3]
        dict1[name_list[4]] = x[4]
        dict1[name_list[5]] = x[5]
        data.append(dict1)

    return render(request, 'product.html',{'data':data})


def productpage(request):
    data = []
    count = -1
    mydb = connection()
    cr = mydb.cursor()
    query = "select * from my_site_product"
    cr.execute(query)
    name_fields = [i[0] for i in cr.description]
    for x in cr:
        count += 1
        dict1 = {}
        dict1[name_fields[0]] = x[0]
        dict1[name_fields[1]] = x[1]
        dict1[name_fields[2]] = x[2]
        dict1[name_fields[3]] = x[3]
        dict1[name_fields[4]] = x[4]
        dict1[name_fields[5]] = x[5]
        dict1['count'] = count
        data.append(dict1)
    return render(request, 'productpage.html', {'data': data})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def usersignup(request):
    name = request.GET['name']
    username = request.GET['username']
    email = request.GET['email']
    password = request.GET['password']

    mydb = connection()
    cr = mydb.cursor()

    # query="create table my_site_usersignup(id int, name varchar(255), username varchar(255), email varchar(50), password varchar(255))"
    # query = "alter table my_site_usersignup MODIFY column username varchar(255) primary key"
    query = "select * from my_site_usersignup where username = '" + username + "'"
    cr.execute(query)
    result = cr.fetchall()
    if len(result) <= 0:
        query = "insert into my_site_usersignup(name,username,email,password) values('" + name + "','" + username + "','" + email + "','" + password + "')"
        cr.execute(query)
        mydb.commit()

    return redirect(login)


def login(request):
    return render(request, 'login.html')


def userlogin(request):
    username = request.GET['username']
    password = request.GET['password']
    data = []
    mydb = connection()
    cr = mydb.cursor()

    query = "select * from my_site_usersignup where username = '" + username + "' and password = '" + password + "'"
    cr.execute(query)
    name_fields = [i[0] for i in cr.description]
    result = cr.fetchall()

    if len(result) != 0:
        for x in result:
            dict1 = {}
            dict1[name_fields[0]] = x[0].title()
            dict1[name_fields[1]] = x[1].title()
            dict1[name_fields[2]] = x[2]
            data.append(dict1)
        request.session['user'] = data

        return redirect(dashboard)
    else:
        return redirect(login)


def dashboard(request):
    if 'user' in request.session:
        data = []
        x = request.session['user']
        mydb = connection()
        cr = mydb.cursor()
        query = "select * from my_site_bill where email = '"+x[0]['email']+"'"
        cr.execute(query)
        name_list = [i[0] for i in cr.description]
        for x in cr:
            dict1 = {}
            dict1[name_list[0]] = x[0]
            dict1[name_list[1]] = x[1]
            dict1[name_list[7]] = x[7]
            dict1[name_list[8]] = x[8]
            dict1[name_list[2]] = x[2]
            data.append(dict1)
        return render(request, 'dashboard.html',{'data':data})
    else:
        return redirect(login)


def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect(login)
    else:
        return redirect(login)

def cartaddition(request):
    id = request.GET['id']
    quantity = int(request.GET['quantity'])
    x = []
    try:
        x = request.session['cart']
    except:
        pass

    query = "select * from my_site_product where id ={}".format(str(id))
    conn = connection()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    d = {
        'id': result[0],
        'name': result[1],
        'price': result[2],
        'discount': result[3],
        'photo': result[4],
        'quantity': quantity,
        'total': result[3]
    }
    if len(x) > 0:

        for row in x:
            if str(id) == str(row['id']):
                return HttpResponse("Already in Cart")
        x.append(d)
    else:
        x.append(d)

    request.session['cart'] = x
    return HttpResponse(len(x))


# def increment(request):
#     global count
#     count += 1
#     return JsonResponse({'count':count},safe=False)


def cartPage(request):
    if 'user' in request.session:
        return render(request, 'cart.html')
    else:
        return redirect(login)

def cartajax(request):
    x = request.session['cart']
    # print(x)
    total = 0
    for data in x:
        total += data['total']
    return JsonResponse({'data': x, 'grand_total': total}, safe=False)


def checkout(request):
    if 'user' in request.session:
        x = request.session['cart']
        grand_total = 0
        for i in x:
            grand_total += i['total']
    # print(x)
        return render(request, 'checkout.html',{'data':x,'grand_total':grand_total})
    else:
        return redirect(index)

def increment(request):
    x = request.session['cart']
    id = request.GET['id']
    s = request.GET['st']
    # print(x)
    if s == '0':
        for data in x:
            if str(data['id']) == str(id):
                val = int(data['quantity'])
                if val > 1:
                    data['quantity'] = val - 1
                    data['total'] = int(data['total']) - int(data['discount'])
    else:
        for data in x:
            if str(data['id']) == str(id):
                val = int(data['quantity'])
                if val < 10:
                    data['quantity'] = val + 1
                    data['total'] = int(data['discount']) * int(data['quantity'])


    request.session['cart'] = x
    # print(x)
    return HttpResponse("success")


def deletecart(request):
    id = request.GET['id']
    x = request.session['cart']

    count = 0
    for data in x:

        if str(data['id']) == str(id):
            del x[count]
        else:
            count += 1
    request.session['cart'] = x
    return HttpResponse("success")


@csrf_exempt
def payment_action(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    country = request.POST['country']
    phone = request.POST['phone']
    email = request.POST['email']
    address = request.POST['address']
    type = request.POST['type']
    total = request.POST['total']
    date1 = date.today()
    mydb = connection()
    cr = mydb.cursor()

    query = f"INSERT INTO `my_site_bill`(`name`, `price`, `email`, `mobile`, `address`, `type`,`status`, `date`) VALUES ('{first_name}',{total},'{email}','{phone}','{address}','{type}', 'pending','{date1}')"

    cr.execute(query)

    id = cr.lastrowid
    x = request.session['cart']
    print(id)

    for row in x:
        query = f"INSERT INTO `my_site_billingdetail`(`bill_id`, `first_name`, `last_name`, `price`, `quantity`, `country`, `address`, `email`, `phone`, `totalprice`, `name`, `photo`) VALUES ({id}, '{first_name}', '{last_name}', '{row['price']}','{row['quantity']}', '{country}', '{address}', '{email}', '{phone}', '{row['total']}','{row['name']}','{row['photo']}')"
        cr.execute(query)
    mydb.commit()
    return JsonResponse({'billid':id})


def thankspage(request):
    data = []
    data2 = []
    id = request.GET['billid']
    mydb = connection()
    cr = mydb.cursor()
    query = "select * from my_site_bill where bill_id = '"+id+"'"
    cr.execute(query)
    name_list = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[7]] = x[7]
        dict1[name_list[8]] = x[8]
        dict1[name_list[2]] = x[2]
        dict1[name_list[6]] = x[6]
        dict1[name_list[5]] = x[5]
        data.append(dict1)
    query = "select name, quantity,price from my_site_billingdetail where bill_id = '"+id+"'"
    cr.execute(query)
    for x in cr:
        dict1 = {}
        dict1['name'] = x[0]
        dict1['quantity'] = x[1]
        dict1['price'] = x[2]
        data2.append(dict1)
    return render(request,'order.html',{'data':data,'data2':data2})

from my_site import models

@csrf_exempt
def getdetails(request):
    id = request.POST['id']
    # print(id)
    mydb = connection()
    cr = mydb.cursor()
    q = 'select * from my_site_billingdetail where bill_id="{}"'.format(id)
    cr.execute(q)
    print(q)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {
            'id': row[1],
            'price': row[4],
            'quantity': row[5],
            'total': row[10],
            'photo': row[12],
            'name': row[11]
        }
        x.append(d)
        print(x)
    return JsonResponse(x, safe=False)


def category(request):
    data = []
    count = -1
    id = request.GET['id']
    mydb = connection()
    cr = mydb.cursor()
    query = "select * from my_site_product where category_id = '"+id+"'"
    cr.execute(query)
    name_fields = [i[0] for i in cr.description]
    for x in cr:
        count += 1
        dict1 = {}
        dict1[name_fields[0]] = x[0]
        dict1[name_fields[1]] = x[1]
        dict1[name_fields[2]] = x[2]
        dict1[name_fields[3]] = x[3]
        dict1[name_fields[4]] = x[4]
        dict1[name_fields[5]] = x[5]
        dict1['count'] = count
        data.append(dict1)
    return render(request, 'productpage.html', {'data': data})

@csrf_exempt
def changepassword(request):
    password = ''
    email = request.session['user'][0]['email']
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    mydb = connection()
    cr = mydb.cursor()
    query = "select password from my_site_usersignup where email = '"+email+"'"
    cr.execute(query)
    result = cr.fetchone()
    for x in result:
        password = x
    if (new_password == confirm_password) and (current_password == password):
        query = "update my_site_usersignup set password = '"+new_password+"' where email = '"+email+"'"
        cr.execute(query)
        mydb.commit()
        messages.success(request,"password changed successfully")
        return HttpResponseRedirect('dashboard')
        # return HttpResponse("success")
    else:
        messages.error(request, "Error in changing password, check your password and try again")
        return HttpResponseRedirect('dashboard')
        # return HttpResponse("failed")