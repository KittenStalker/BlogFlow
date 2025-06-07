from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (('Draft', 'draft'), ('Published', 'published'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    postDate = models.DateField(default=timezone.now)

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    content = models.TextField(blank=True, max_length=5000)

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self) -> str:  #для отображения
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})