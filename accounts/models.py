from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.

# This is just basically extending the django user model to accomodate more fields in the future


class CustomUser(AbstractUser):
    profile_pic = CloudinaryField('image', blank=True, null=True)
