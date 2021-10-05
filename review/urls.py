from django.urls import path
from . import views
from .views import *

app_name = "review"
urlpatterns = [
    path('',views.review,name='review'),
    path('<int:id>/',views.filter,name='filter'),

    # 검색
    path('search/', views.SearchReview, name="SearchReview")
]