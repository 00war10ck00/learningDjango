from django.http import HttpResponse
from django.shortcuts import render,redirect
from sqlite3 import *

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
    return render(request,'index.html',{'data':data,'data1':data1})


def product(request):
    return render(request,'product.html')


def productpage(request):
    return render(request,'productpage.html')