from django.shortcuts import render
from restaurant.views import *

def main(request):
  review = Comment.objects.all()
  id_arr = []
  if len(review) < 6:
    review = review.order_by("-like_users","-created_at")
  else:
    review = review.order_by("-like_users","-created_at")
    for i in range(6):
      id_arr.append(review[i].id)
    review = review.filter(id__in=id_arr)
  return render(request, 'mainPage.html',{'review':review})