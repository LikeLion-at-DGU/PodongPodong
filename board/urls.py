from django.urls import path
from .views import *

app_name = 'board'
urlpatterns = [
    path('board_main',board_main,name='board_main'),
    path('request_detail/<str:id>',request_detail,name='request_detail'),
    path('request_edit/<str:id>',request_edit,name='request_edit'),
    path('request_update/<str:id>',request_update,name='request_update'),
    path('request_delete/<str:id>',request_delete,name='request_delete'),
    path('request_create',request_create,name='request_create'),
]