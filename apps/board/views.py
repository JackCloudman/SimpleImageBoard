from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Board,Post
# Create your views here.
def index(request):
    return render(request,'board/index.html',{})
def showboard(request,board):
    b = get_object_or_404(Board, name=board)
    posts = Post.objects.filter(board=b).order_by('created_date')
    return render(request,'post/list.html',{'posts':posts,'board':b})
