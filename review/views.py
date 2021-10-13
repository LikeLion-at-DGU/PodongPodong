from typing import Counter
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from restaurant.models import Comment, Category

from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def review(request):
    reviews = Comment.objects.all().annotate(like_count = Count('like_users')).order_by("-like_count", "-created_at")
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
    reviews = Comment.objects.filter(restaurant__category__id__contains = id).annotate(like_count = Count('like_users')).order_by("-like_count", "-created_at")
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
    search_category = request.GET.get('category')
    search_key = request.GET.get('search_key')
    reviews = Comment.objects.all().annotate(like_count = Count('like_users')).order_by("-like_count", "-created_at")
    category = Category.objects.all()
    if search_key:
        if search_category == "restaurant":
            reviews = reviews.filter(Q(restaurant__name__icontains=search_key))
        elif search_category == "writer":
            reviews = reviews.filter(Q(user__username__icontains=search_key))
        else:
            reviews = reviews.filter(Q(content__icontains=search_key))
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
