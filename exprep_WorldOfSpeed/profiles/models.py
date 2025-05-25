from django.db import models
from .validators import CustomMinCharValidator, AlphaNumericandUnderscoreValidator
from django.core.validators import MinValueValidator

# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            CustomMinCharValidator(),
            AlphaNumericandUnderscoreValidator(),
        ]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[
            MinValueValidator(21),
        ]
    )
    password = models.CharField(
        max_length=20,
    )
    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )