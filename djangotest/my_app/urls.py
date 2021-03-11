from django.urls import path
from .views import *


urlpatterns = [
    path("home",myHome, name="ram")
]
