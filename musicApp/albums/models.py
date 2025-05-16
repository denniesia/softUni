from django.db import models
from .choices import GenreChoices
from django.core.validators import MinValueValidator
# Create your models here.
class Album(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=GenreChoices,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ]
    )
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )