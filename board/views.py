from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone


# Create your views here.

def board_main(request):
    boards = Board.objects.all()
    return render(request,'board/board_main.html',{'board':boards})

def request_detail(request,id):
    board = get_object_or_404(Board,pk=id)
    return render(request,'board/request_detail.html',{'board':board})

def request_new(request):
    return render(request,'board/request_new.html')

def request_create(request):
    request_new_post = Board()
    request_new_post.title = request.POST['title']
    request_new_post.cafeteria = request.POST['cafeteria']
    request_new_post.writer = request.user
    request_new_post.date = timezone.now()
    request_new_post.body = request.POST['body']
    request_new_post.save()
    return redirect('board:request_detail',request_new_post.id)

def request_edit(request,id):
    request_edit_post = Board.objects.get(id = id)
    return render(request, 'board/request_edit.html', {'board':request_edit_post})

def request_update(request,id):
    request_update_post = get_object_or_404(Board, id = id)
    request_update_post.title = request.POST['title']
    request_update_post.cafeteria = request.POST['cafeteria']
    request_update_post.writer = request.user
    request_update_post.date = timezone.now()
    request_update_post.body = request.POST['body']
    request_update_post.save()
    return redirect('board:request_detail',request_update_post.id)

def request_delete(request,id):
    request_delete_post = Board.objects.get(id = id)
    request_delete_post.delete()
    return redirect('board:board_main')