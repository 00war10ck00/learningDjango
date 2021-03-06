from django.http import HttpResponse
from django.shortcuts import render, redirect
from connection import connections
from django.contrib import messages
import random
from django.core.files.storage import FileSystemStorage


def public_home(request):
    return render(request, 'public_home.html')


def signup(request):
    return render(request, 'signup.html')


def register(request):
    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    mobile = request.POST['mobile']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(f"images/{random.randint(0, 1000)}{photo.name}", photo)
    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url)
    mydb = connections.conn
    cr = mydb.cursor()

    query = "select username from signup where username = '" + username + "'"
    cr.execute(query)
    rows = cr.rowcount
    # print(cr.rowcount)
    # for x in cr:
    #     print(x)
    if rows == 1:
        messages.warning(request, "Signup Failed - Username Already Exist")
        # return HttpResponse("Failed")
        return redirect(signup)

    else:
        query = "insert into signup(username,name,email,password,gender,mobile,photo) values('" + username + "','" + name + "','" + email + "','" + password + "','" + gender + "','" + mobile + "','" + uploaded_file_url + "')"
        cr.execute(query)
        mydb.commit()
        messages.da(request, "Signup Successfull")
        return redirect(login_page)
        # return HttpResponse("sucess")


def login_page(request):
    return render(request, 'login.html')


def login(request):
    name = request.POST['username']
    password = request.POST['password']

    mydb = connections.conn
    cr = mydb.cursor()
    data = []
    query = "select * from signup where username='" + name + "' and password = '" + password + "'"
    cr.execute(query)
    if cr.rowcount == 1:
        for x in cr:
            data = [x[0], x[1], x[6]]
            request.session['admin'] = data
        # return HttpResponse("sucess")
        messages.success(request, 'Login Successfull')
        return redirect(dashboard)
    else:
        messages.warning(request, 'Invalid Username/Password')
        messages.error(request, 'Invalid Username/Password')
        # return render(request, 'login.html')
        return redirect(login_page)

def dashboard(request):
    if 'admin' in request.session:
        return render(request, 'dashboard.html')
    else:
        return redirect(login_page)


def logout(request):
    del request.session['admin']
    messages.success(request, 'Log Out Successfully')
    return redirect(login_page)


def addcontact(request):
    if 'admin' in request.session:
        return render(request, 'addcontact.html')
    else:
        return redirect(login_page)


def contact_addition(request):
    mydb = connections.conn
    cr = mydb.cursor()
    username = request.POST['username']
    contactname = request.POST['contactname']
    mobile = request.POST['mobile']
    email = request.POST['email']
    file = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(f"images/{random.randint(1, 1000)}{file.name}", file)
    uploaded_file_url = fs.url(filename)
    query = "insert into contacts(username,contactname,mobile,email,photo) values('" + username + "','" + contactname + "','" + mobile + "','" + email + "','" + uploaded_file_url + "')"

    cr.execute(query)

    mydb.commit()
    messages.success(request, 'Added Successfully')
    return redirect(addcontact)


def contact_view_page(request):
    # return render(request,'viewcontact.html')
    if 'admin' in request.session:
        return redirect(view_contact)
    else:
        return redirect(login_page)


def view_contact(request):
    data = []
    mydb = connections.conn
    cr = mydb.cursor()
    username = request.session['admin'][0]
    # print(username)
    query = "select * from contacts where username = '" + username + "'"
    cr.execute(query)
    field_names = [i[0] for i in cr.description]
    # print(field_names)
    for x in cr:
        dict1 = {}
        dict1[field_names[0]] = x[0]
        dict1[field_names[1]] = x[1]
        dict1[field_names[2]] = x[2]
        dict1[field_names[3]] = x[3]
        dict1[field_names[4]] = x[4]
        dict1[field_names[5]] = x[5]
        data.append(dict1)
    return render(request, 'viewcontact.html', {'data': data})
