from django.contrib import admin
from .models import user_account, image, favicon

# Register your models here.
admin.site.register(user_account)
admin.site.register(image)
admin.site.register(favicon)