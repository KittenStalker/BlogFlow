from django.db import models
from django.utils import timezone

from .user import User
from .post import Post

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

    content = models.TextField()

    postDate = models.DateField(default=timezone.now)

    def __repr__(self) -> str:  #для отладки
        return f'Comment #{self.id} | in {self.blog} on {self.postDate}'

    def __str__(self) -> str:  #для отображения
        return f'Comment in "{self.blog}" by {self.user} on {self.date}'