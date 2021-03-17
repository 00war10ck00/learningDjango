from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from sqlite3 import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

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
    return render(request, 'product.html')


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
            dict1[name_fields[1]] = x[1].title()
            dict1[name_fields[2]] = x[2]
            dict1[name_fields[3]] = x[3]
            data.append(dict1)
        request.session['user'] = data
        return redirect(dashboard)
    else:
        return redirect(login)


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    del request.session['user']
    return redirect(login)


def cartaddition(request):
    id = request.GET['id']
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
        'quantity': 1,
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
    return render(request, 'cart.html')


def cartajax(request):
    x = request.session['cart']
    # print(x)
    total = 0
    for data in x:
        total += data['total']
    return JsonResponse({'data': x, 'grand_total': total}, safe=False)


def checkout(request):
    x = request.session['cart']
    grand_total = 0
    for i in x:
        grand_total += i['total']
    # print(x)
    return render(request, 'checkout.html',{'data':x,'grand_total':grand_total})


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

    mydb = connection()
    cr = mydb.cursor()
    query = f"INSERT INTO `my_site_bill`(`name`, `price`, `email`, `mobile`, `address`, `type`) VALUES ('{first_name}',{total},'{email}','{phone}','{address}','{type}')"

    cr.execute(query)

    id = cr.lastrowid
    x = request.session['cart']
    print(id)

    for row in x:
        query = f"INSERT INTO `my_site_billdetail`(`billid`, `first_name`, `last_name`, `price`, `qunatity`, `country`, `address`, `email`, `phone`, `totalprice`, `name`, `photo`) VALUES ({id}, '{first_name}', '{last_name}' '{row['price']}','{row['quantity']}', '{country}', '{address}', '{email}', '{phone}' '{row['total']}','{row['name']}','{row['photo']}')"
        cr.execute(query)
    mydb.commit()
    return JsonResponse({'billid':id})
