from django.http import HttpResponse
from django.shortcuts import render
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

def getData(request):
    name = request.POST['Name']
    Class = request.POST['class']
    mobile = request.POST['mobile']
    # img = request.FILES['img']
    # print(img)
    print(request.POST)
    for i in request.POST:
        print(f"{i}->",request.POST[i])
    return render(request,'demo.html',{'data':request.POST})
    # return HttpResponse(f"Success {name},{Class},{mobile},{request.POST}")
