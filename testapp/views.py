from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Админ',
        'title': 'Это первый пост',
        'description': 'Описание',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022',
        'views': '123',
    },
    {
        'author': 'Админ',
        'title': 'Это первый пост',
        'description': 'Описание',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022',
        'views': '123',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse('<h1>Наш клуб</h1>')

def user(request, username):
    return HttpResponse(f"By {username}")

def single_post(request, username, postid):
    return HttpResponse(f"<h2>{username} - {postid}</h2>")



