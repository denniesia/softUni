from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import OnlyLettersValidator, MaxDigitsValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            OnlyLettersValidator()
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator()
        ]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[
            MinLengthValidator(6),
            MaxDigitsValidator
        ]
    )
    pets_numbers = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
