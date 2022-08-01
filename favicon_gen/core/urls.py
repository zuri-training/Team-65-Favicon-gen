from django.urls import path
from .views import dashBoardView, deleteImageView, imageListView, imageUploadView, downloadFaviconView

app_name = 'core'

urlpatterns = [
    path('', dashBoardView,  name='dashboard'),
    path('my-images/', imageListView, name='image-list'),
    path('upload/', imageUploadView, name='upload'),
    path('favicon/<int:pk>/', downloadFaviconView, name='download'),
    path('delete/<int:pk>/', deleteImageView, name='delete-favicon'),
]
