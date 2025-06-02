from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path("user/<username>", views.user, name='blog-user'),
	path('post/<username>/<postid>', views.single_post, name='blog-post'),
]