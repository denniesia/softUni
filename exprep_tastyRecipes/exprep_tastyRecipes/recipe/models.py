from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .choices import CuisineTypes

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(10),
        ]
    )
    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypes,
    )
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ]
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
    )