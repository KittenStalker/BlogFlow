from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def user(request, username):
    return HttpResponse(f"By {username}")

def single_post(request, username, postid):
    return HttpResponse(f"<h2>{username} - {postid}</h2>")



