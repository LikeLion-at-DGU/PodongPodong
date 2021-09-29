from django.urls import path
from . import views
from .views import RestaurantList, CreateRestaurantComment

app_name = "restaurant"
urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('<str:id>/', RestaurantList, name='restaurant_list2'),
    path('detail/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('<int:id>/create_comment', CreateRestaurantComment, name="create_restaurant_comment"),
]