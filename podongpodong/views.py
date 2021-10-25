from django.shortcuts import render
from restaurant.views import *
from django.db.models import Count

def main(request):
  review = Comment.objects.all()
  id_arr = []
  if len(review) < 6:
    review = review.annotate(like_count = Count('like_users')).order_by("-like_count", "-created_at")
  else:
    review = review.annotate(like_count = Count('like_users')).order_by("-like_count", "-created_at")
    for i in range(6):
      id_arr.append(review[i].id)
    review = review.filter(id__in=id_arr)
  category = Category.objects.all()
  return render(request, 'mainPage.html',{'review':review, 'category':category})