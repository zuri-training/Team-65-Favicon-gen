from django.urls import path
from .views import AboutPageView, ContactPageView, dashBoardView, deleteImageView, imageUploadView

app_name = 'core'

urlpatterns = [
    path('', dashBoardView,  name='dashboard'),
    path('my-favicons/', imageUploadView, name='upload'),
    path('delete/<int:pk>/', deleteImageView, name='delete-favicon'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
