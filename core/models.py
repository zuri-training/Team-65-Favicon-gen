from django.db import models
from accounts.models import CustomUser


class Image(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image_url = models.TextField()
    image_upload_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-image_upload_date',)

    def __str__(self):
        return self.image_name


class Favicon_Zip(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_id = models.OneToOneField(Image, on_delete=models.CASCADE)
    favicon_name = models.CharField(max_length=50)
    favicon_zip_url = models.TextField()
    favicon_creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.favicon_name
