"""Apparel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Ad`d a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index),
    path('productpage',productpage),
    path('product',product),
    path('login',login),
    path('register',register),
    path('usersignup',usersignup),
    path('userlogin',userlogin),
    path('dashboard',dashboard),
    path('logout',logout),
    path('cartaddition',cartaddition, name="cartaddition"),
    path('cartPage',cartPage),
    path('cartajax',cartajax),
    path('login',login),
    path('checkout',checkout),
]
