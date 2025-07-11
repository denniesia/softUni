from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    pages = models.PositiveIntegerField()
    description = models.TextField(
        max_length=100,
        default=""
    )
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title