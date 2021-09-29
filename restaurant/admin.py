from django.contrib import admin
from restaurant.models import Category, Restaurant, FoodMenu, Comment

admin.site.register([Category, Restaurant, FoodMenu, Comment])