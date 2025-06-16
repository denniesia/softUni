from django.db import models
from django.core.validators import MinLengthValidator
from .validators import CapitalizeFirstNameValidator

# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(2, 'Nickname must be at least 2 chars long')
        ],
    )
    first_name = models.CharField(
        max_length=30,
        validators=[
            CapitalizeFirstNameValidator()
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            CapitalizeFirstNameValidator()
        ]
    )
    chef = models.BooleanField(
        default=False
    )
    bio = models.TextField(
        blank=True,
        null=True
    )