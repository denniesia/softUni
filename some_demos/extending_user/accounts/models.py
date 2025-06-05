from django.db import models
from django.contrib.auth import get_user_model, models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import AccountUserManager

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
# UserModel = get_user_model()
# class Profile(models.Model):
#     age = models.PositiveIntegerField(
#         blank=True,
#         null=True,
#     )
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.DO_NOTHING,
#         primary_key=True,
#     )

'''
2.2. Create your own user model:
Pros:
- Easier migration to other auth model in the future
'''
#info related to the auth processes
class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin): #AbstractBaseUser provides the password part of the **credentials
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    #this is the second part og the **credentials
    USERNAME_FIELD = 'email'

    objects = AccountUserManager()


#personal info of the user
class Profile(models.Model):
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AccountUser,
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )
