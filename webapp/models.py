from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class user_account(models.Model):

    # DB Fields
    user_account_id = models.CharField(primary_key=True, max_length=255)
    user_account_email_address = models.EmailField(max_length=255, unique=True, blank=False)
    user_account_password = models.CharField(max_length=255, blank=False)
    user_account_phone_number = models.CharField(max_length=10, unique=True, blank=False)
    user_account_security_question = models.CharField(max_length=255, blank=False)
    user_account_security_answer = models.CharField(max_length=255, blank=False)
    user_account_image_url = models.CharField(max_length=255)
    user_account_color = models.CharField(max_length=6, default='ffffff')
    user_account_theme = models.BinaryField(default=0)
    user_account_is_active = models.BinaryField(default=1)
    user_account_creation_date = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ("-user_account_creation_date",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_account_email_address)
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.user_account_email_address
    
    # def get_absolute_url(self):
    #     return reverse("blog:post_detail", kwargs={"slug": self.slug})


class image(models.Model):

    # DB Fields
    image_id = models.CharField(primary_key=True, max_length=255)
    user_account_id = models.ForeignKey(user_account, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)
    image_file_type = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)
    image_upload_date = models.DateTimeField(auto_now_add=True)
    media = models.ImageField(null=True, blank=True, upload_to='images/')


    class Meta:
        ordering = ("-image_upload_date",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.image_name)
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.image_name
    


class favicon(models.Model):

    # DB Fields
    favicon_id = models.CharField(primary_key=True, max_length=255)
    user_account_id = models.ForeignKey(user_account, on_delete=models.CASCADE)
    image_id = models.ForeignKey(image, on_delete=models.CASCADE)
    favicon_name = models.CharField(max_length=255)
    favicon_path = models.CharField(max_length=255)
    favicon_creation_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ("-favicon_creation_date",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.favicon_name)
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.favicon_name
    
