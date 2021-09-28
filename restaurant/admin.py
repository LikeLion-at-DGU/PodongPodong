from django.contrib import admin
from restaurant.models import Category, Restaurant

admin.site.register([Category, Restaurant])