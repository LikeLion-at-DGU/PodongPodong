from django.shortcuts import render
from restaurant.views import *

def main(request):
  review = Comment.objects.all()
  return render(request, 'mainPage.html',{'review':review})