from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    # data = Question.objects.all()
    # print(data)
    return HttpResponse("<h1>Hello World Its index Page</h1>")


def contact(request):
    return HttpResponse("<h1>Hello World Its contact Page</h1>")


def about(request):
    return HttpResponse("<h1>Hello World Its about Page</h1>")
