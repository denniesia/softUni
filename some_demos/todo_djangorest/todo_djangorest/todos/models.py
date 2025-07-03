
from django.contrib.auth import get_user_model
from django.db import models
from .choices import StateChoices
# Create your models here.

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=15)

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    state = models.BooleanField(
        choices=[
           ( True, StateChoices.DONE),
           (False, StateChoices.NOT_DONE),
        ],
        default=False
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    assignees = models.ManyToManyField(
        UserModel,
        related_name='assigned_todos',
        blank=True,
    )

    def __str__(self):
        self.title