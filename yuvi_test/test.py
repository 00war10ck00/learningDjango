from django.http import HttpResponse
from django.shortcuts import render
from random import randint
import math
def index(request):
    return HttpResponse("Hello World")
def indexpage(request):
    # data = {"name":"yuvraj","class":10}
    data = ["yuvraj",10,"arora"]
    # return render(request,"test1.html",{'data':data})
    return render(request,"test1.html",{'data':data})
def factorial(request):
    data = randint(1,50)
    return HttpResponse("Random number is"+" "+str(data)+"<br>Factorial of number is "+str(math.factorial(data)))

def table(request):
    data = randint(1,20)
    str1 = ""
    for i in range(1,16):
        str1 = str1 + str(data)+ " X "+str(i)+" = "+str(data*i)+"<br>"
    # print(str1)
    return HttpResponse("Random number is"+" "+str(data)+"<br>Table:<br>"+str1)


def table1(request):
    list1 = []
    num = 5
    for i in range(1,11):
        dict1 = {}
        data = num*i
        dict1["num"] = num
        dict1["i"] = i
        dict1["ans"] = data
        list1.append(dict1)
    # print(list1)
    # return HttpResponse(list1)
    return render(request,"test1.html",{"list1":list1})
