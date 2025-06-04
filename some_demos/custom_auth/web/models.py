from django.db import models

# Create your models here.

#no table needed
class AuditModel:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Model1(AuditModel, models.Model):
    field = models.CharField(max_length=100)