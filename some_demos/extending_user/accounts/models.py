from django.db import models
from django.contrib.auth import get_user_model, models as auth_models

# Create your models here.
#UserModel = get_user_model()

'''
1. Extend the built-in user model through 'AbstractUser':
- Add 'age' field
- Add 'gender' field

Pros:
- Simpler
- No need to rewrite Django auth system
'''

class CustomUser(auth_models.AbstractUser):
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )