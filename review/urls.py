from django.urls import path
from . import views
from .views import *

app_name = "review"
urlpatterns = [
    path('',views.review,name='review'),
]