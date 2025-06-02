from django.contrib import admin
from .models import Post, Comment

@admin.register(Post, Comment)
class BlogAdmin(admin.ModelAdmin):
    pass

