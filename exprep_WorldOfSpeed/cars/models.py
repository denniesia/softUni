from django.db import models
from .choices import CarTypes
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import RangeValidator

# Create your models here.
class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypes,
    )
    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1),
        ]
    )
    year = models.IntegerField(
        validators=[
            RangeValidator()
        ]
    )
    image_url = models.URLField(
        unique=True,
    )
    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars',
    )