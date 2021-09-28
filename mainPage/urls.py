from django.urls import path
from .views import *

app_name = "mainPage"
urlpatterns = [
    path('', main, name="main"),
]