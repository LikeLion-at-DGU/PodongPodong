from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from restaurant.models import *

from django.db.models import Q

# Create your views here.

def review(request):
    reviews = Comment.objects.all().order_by("-created_at")
    category = Category.objects.all()
    user = request.user
    return render(request, "review.html",{'reviews':reviews, 'user':user, 'category':category})

def filter(request, id): 
    reviews = Comment.objects.filter(restaurant__category__id__contains = id).order_by("-created_at")
    category = Category.objects.all()
    user = request.user
    return render(request, "filter.html",{'reviews':reviews, 'user':user, 'category':category})

def SearchReview(request):
    search_key = request.GET.get('search_key')
    reviews = Comment.objects.all()
    category = Category.objects.all()
    if search_key:
        reviews = reviews.filter(Q(content__icontains=search_key)).distinct().order_by('-id')
    return render(request, "search.html", { 'reviews': reviews, 'category': category })