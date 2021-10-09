from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from restaurant.models import Comment, Category

from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def review(request):
    reviews = Comment.objects.all().order_by("-like_users", "-created_at")
    category = Category.objects.all()
    user = request.user
    paginator = Paginator(reviews, 10)
    page = request.GET.get("page") or 1
    pages = pages = paginator.get_page(page)
    context = {
        'reviews':reviews,
        'user':user,
        'category':category,
        'pages':pages,
    }
    return render(request, "review.html",context)

def filter(request, id): 
    reviews = Comment.objects.filter(restaurant__category__id__contains = id).order_by("-like_users", "-created_at")
    category = Category.objects.all()
    user = request.user
    paginator = Paginator(reviews, 10)
    page = request.GET.get("page") or 1
    pages = pages = paginator.get_page(page)
    context = {
        'reviews':reviews,
        'user':user,
        'category':category,
        'pages':pages,
    }
    return render(request, "filter.html",context)

def SearchReview(request):
    search_key = request.GET.get('search_key')
    reviews = Comment.objects.all()
    category = Category.objects.all()
    if search_key:
        reviews = reviews.filter(Q(content__icontains=search_key)).distinct().order_by('-id')
    paginator = Paginator(reviews, 10)
    page = request.GET.get("page") or 1
    pages = paginator.get_page(page)
    context = {
        'reviews': reviews,
        'category': category, 
        'search_key': search_key, 
        'pages': pages
    }
    return render(request, "search.html", context)