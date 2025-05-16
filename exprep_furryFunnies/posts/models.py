from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ],
        unique=True,
    )
    image_url = models.URLField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        to='authors.Author',
        on_delete=models.CASCADE,
        related_name='posts',
    )