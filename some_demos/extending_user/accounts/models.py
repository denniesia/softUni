from django.db import models
from django.contrib.auth import get_user_model, models as auth_models

# Create your models here.


'''
1. Extend the built-in user model through 'AbstractUser':
- Add 'age' field
- Add 'gender' field

Pros:
- Simpler
- No need to rewrite Django auth system
'''

# class CustomUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField(
#         blank=True,
#         null=True,
#     )

'''
2. Extend the user model through a One-to-One relationship with 'Profile' model:
- Add 'age' field
- Add 'gender' field
...

2.1 Use the built-in user model for auth
'''
UserModel = get_user_model()
class Profile(models.Model):
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )