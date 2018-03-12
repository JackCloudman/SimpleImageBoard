from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render,redirect
from .models import Board,Post
from apps.board.forms import PostForm  
# Create your views here.
def index(request):
    return render(request,'board/index.html',{})
def showboard(request,board):
    b = get_object_or_404(Board, name=board)
    posts = Post.objects.filter(board=b).order_by('-created_date')
    return render(request,'post/list.html',{'posts':posts,'board':b})
def boardlist(request):
    boards = Board.objects.all()
    return render(request,'boards.html',{'boards':boards}) 
def new_post(request,board):
    b = get_object_or_404(Board, name=board)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.board = b
            post.save()
            return redirect("/"+board+"/")
    else:
        form = PostForm()
    return render(request,'post/new_post.html',{'form':form,'board':b})
