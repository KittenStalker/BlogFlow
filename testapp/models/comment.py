from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from .post import Post

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content = models.TextField()

    postDate = models.DateField(default=timezone.now)

    def __repr__(self) -> str:  #для отладки
        return f'Comment #{self.id} | in {self.post} on {self.postDate}'

    def __str__(self) -> str:  #для отображения
        return f'Comment in "{self.post}" by {self.user} on {self.postDate}'