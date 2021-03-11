from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from connection import connections
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages

list1 = []


def view(request):
    data = []
    mydb = connections.conn
    cr = mydb.cursor()
    query = "select * from products"
    cr.execute(query)
    result = cr.fetchall()
    name_fields = [i[0] for i in cr.description]
    for x in result:
        dict1 = {}
        dict1[name_fields[0]] = x[0]
        dict1[name_fields[1]] = x[1].title()
        dict1[name_fields[2]] = x[2]
        dict1[name_fields[3]] = x[3]
        dict1[name_fields[4]] = x[4]
        # dict[name_fields[5]] = x[5]
        data.append(dict1)
    print(data)
    return render(request, 'index.html', {'data': data})


def product_page(request):
    data = []
    id = request.GET['btn']
    mydb = connections.conn
    cr = mydb.cursor()

    query = "select * from products where p_id = '" + id + "'"
    cr.execute(query)
    name_list = [i[0] for i in cr.description]
    for x in cr:
        dict1 = {}
        dict1[name_list[0]] = x[0]
        dict1[name_list[1]] = x[1].title()
        dict1[name_list[2]] = x[2]
        dict1[name_list[3]] = x[3]
        dict1[name_list[4]] = x[4]
        data.append(dict1)

    return render(request, 'product_page.html', {'data': data})


def cart_addition(request):
    id = request.GET['p_id']
    quantity = request.GET['quantity']
    mydb = connections.conn
    cr = mydb.cursor()
    # print(id)
    query = "select * from products where p_id = '" + id + "'"
    cr.execute(query)
    name_list = [i[0] for i in cr.description]
    # print(name_list)

    if 'cart' in request.session:
        x = request.session['cart']
        for row in x:
            # print(type(row['p_id']))
            # print(type(id))
            if str(row['p_id']) == str(id):
                # return HttpResponse("Allready")
                # print("sucess")
                messages.warning(request, "already present in cart")
                return HttpResponseRedirect('product_page?btn=' + str(id))
    list2 = []
    for x in cr:
        data = {}
        data[name_list[0]] = x[0]
        data[name_list[1]] = x[1].title()
        data[name_list[2]] = x[2]
        data[name_list[3]] = x[3]
        data[name_list[4]] = x[4]
        data['quantity'] = quantity
        data['total_price'] = int(data['product_price']) * int(data['quantity'])
        list1.append(data)
        list2 = []
        list2.append(data)
    # print(list1)

    request.session['cart'] = list1
    # print(request.session['admin'])
    return render(request, 'product_page.html', {'data': list2})


def cart(request):
    return render(request, 'cart.html')


def cartajax(request):
    x = request.session['cart']
    # print(x)
    total = 0
    for data in x:
        total += data['total_price']
    return JsonResponse({'data':x,'total':total}, safe=False)


def increment(request):
    x = request.session['cart']
    id = request.GET['id']
    s = request.GET['st']

    if s == '0':
        for data in x:
            if str(data['p_id']) == str(id):
                val = int(data['quantity'])
                if val > 1:
                    data['quantity'] = val - 1
                    data['total_price'] = int(data['total_price']) - int(data['product_price'])
    else:
        for data in x:
            if str(data['p_id']) == str(id):
                val = int(data['quantity'])
                if val < 10:
                    data['quantity'] = val + 1
                    data['total_price'] = int(data['product_price']) * int(data['quantity'])


    request.session['cart'] = x
    # print(x)
    return HttpResponse("success")

def deletecart(request):
    id = request.GET['pid']
    x = request.session['cart']
    count = 0
    for data in x:
        if str(data['p_id']) == str(id):
            del x[count]
        else:
            count += 1


    request.session['cart'] = x
    return HttpResponse("success")

# def showAjexPage(request):
#     return render(request, 'teachingAJAX.html')
#
#
# def showAjexPageResponse(request):
#     mydb = connections.conn
#     cr = mydb.cursor()
#     query = "select * from products"
#     cr.execute(query)
#     result = cr.fetchall()
#     print(result)
#     return JsonResponse(result, safe=False)

def checkout(request):
    x = request.session['cart']
    total = 0
    for data in x:
        total += data['total_price']
    return render(request, 'checkout.html',{'total':total})

@csrf_exempt
def payment_action(request):
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    address = request.POST['address']
    type = request.POST['type']
    total = request.POST['total']

    mydb = connections.conn
    cr = mydb.cursor()
    query = f"INSERT INTO `bill`(`name`, `price`, `email`, `mobile`, `address`, `type`) VALUES ('{name}',{total},'{email}','{mobile}','{address}','{type}')"

    cr.execute(query)

    id = cr.lastrowid
    x = request.session['cart']
    print(id)

    for row in x:
        query = f"INSERT INTO `billDetail`(`billid`, `price`, `qty`, `totalprice`, `picture`, `name`) VALUES ({id},'{row['product_price']}','{row['quantity']}','{row['total_price']}','{row['photo']}','{row['product_name']}')"
        cr.execute(query)
    mydb.commit()
    return JsonResponse({'billid':id})


def thankspage(request):
    try:
        del request.session['cart']
    except:
        pass
    id = request.GET['billid']
    return render(request,'thankspage.html',{'id':id})