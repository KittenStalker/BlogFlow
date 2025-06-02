from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (('Draft', 'draft'), ('Published', 'published'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    postDate = models.DateField(default=timezone.now)

    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    content = models.TextField(blank=True)

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __repr__(self) -> str:  #для отладки
        return f'Post #{self.id} | by {self.user} | {self.title}, {self.postDate}'

    def __str__(self) -> str:  #для отображения
        return f'"{self.title}" by {self.user} on {self.postDate}'