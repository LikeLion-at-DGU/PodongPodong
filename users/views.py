from django.shortcuts import render
from board.models import Board
from django.contrib.auth.models import User
# Create your views here.

def mypage(request,id):
    user = request.user
    context = {
        'user':user,
        'boards':Board.objects.filter(writer=user).order_by('-date'),
    }
    return render(request, 'users/mypage.html',context)