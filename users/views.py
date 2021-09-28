from django.shortcuts import render
from board.models import Board
from django.contrib.auth.models import User

# Create your views here.

def mypage(request):
    user = request.user
    boards = Board.objects.filter(writer = user)
    return render(request,'users/mymage.html',{'boards':boards})