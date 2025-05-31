from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    reputation = models.PositiveIntegerField(default=0)

    regDate = models.DateField(default=timezone.now)
    birthday = models.DateField(null=True)

    def increment_reputation(self):
        self.reputation += 1
        self.save(update_fields=['reputation'])

    def __repr__(self) -> str:  #для отладки
        return f'User #{self.id} | {self.name}'

    def __str__(self) -> str:  #для отображения
        return f'User #{self.id} | {self.name}'