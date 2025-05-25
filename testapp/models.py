from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(null=True) #12.12.12 12:12
    comment = models.CharField(max_length=200)
    birthday = models.DateField(null=True)

    def __str__(self) -> str:
        return f'{self.name}'