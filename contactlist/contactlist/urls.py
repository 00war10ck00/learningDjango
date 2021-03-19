"""contactlist URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_home),
    path('signup',signup),
    path('register',register),
    path('login_page',login_page),
    path('login',login),
    path('dashboard',dashboard),
    path('logout',logout),
    path('addcontact',addcontact),
    path('contact_addition',contact_addition),
    path('contact_view_page',contact_view_page),
    path('view_contact',view_contact)
]
