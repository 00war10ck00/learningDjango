from django.http import HttpResponse
from django.shortcuts import render, redirect
from connection import connections
import pymysql
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def signup(request):
    return render(request, 'signup.html')


def register(request):
    email = request.POST['email']
    name = request.POST['name']
    password = request.POST['password']
    file = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(f"image/{file.name}", file)
    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url)
    # print(file)
    # print(request.POST)

    mydb = connections.conn
    cr = mydb.cursor()
    query = "insert into signup(email,name,secret_key,photo) values('" + email + "','" + name + "','" + password + "','" + uploaded_file_url + "')"
    cr.execute(query)
    mydb.commit()

    messages.success(request,'Signup Successfull')
    # return HttpResponse(f"Success {name},{email},{password},{file}")
    # return render(request, 'login.html')
    return redirect(login_page)

def login_page(request):
    if 'admin' in request.session:
        return redirect(dashboard)
    return render(request,'login.html')

def logout(request):
    del request.session['admin']
    return redirect(login_page)

def login(request):

    data = []
    mydb = connections.conn
    cr = mydb.cursor()
    name = request.POST['name']
    password = request.POST['password']

    query = "select * from signup where name='" + name + "' and secret_key ='" + password + "'"

    cr.execute(query)
    # for x in cr:
    #     print(x[1])
    print(cr.rowcount)
    if cr.rowcount == 1:
        for x in cr:
            data = [x[1],x[2],x[4]]
            request.session['admin'] = data
            return redirect(dashboard)
    else:
        return render(request, 'login.html')


def dashboard(request):
    if 'admin' in request.session:
        return render(request,'dashboard.html')
    else:
        return redirect(login_page)
def login1Page(request):
    return render(request,'login1.html')

def login1(request):
    return HttpResponse("SUCCESSS")