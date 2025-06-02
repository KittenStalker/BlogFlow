from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class NewUser(models.Model):
    description = models.TextField(blank=True, max_length=200)
    reputation = models.PositiveIntegerField(default=0)

    birthday = models.DateField(null=True)

    def increment_reputation(self):
        self.reputation += 1
        self.save(update_fields=['reputation'])
