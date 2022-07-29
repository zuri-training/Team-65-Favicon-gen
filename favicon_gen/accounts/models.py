from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#This is just basically extending the django user model to accomodate more fields in the future
class CustomUser(AbstractUser):
    country = models.CharField(blank=True, null=True, max_length=30)
