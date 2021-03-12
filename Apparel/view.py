from django.http import HttpResponse
from django.shortcuts import render,redirect
from sqlite3 import *
def connection():
    conn = connect('db.sqlite3')
    return conn

def index(request):
    mydb = connection()
    cr = mydb.cursor()
    query = "create table category("
    return render(request,'index.html')