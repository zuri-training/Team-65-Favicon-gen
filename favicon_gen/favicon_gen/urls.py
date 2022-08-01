from unicodedata import name
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='core'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]
