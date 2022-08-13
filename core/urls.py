from django.urls import path
from .views import AboutPageView, ContactPageView, FAQPageView, dashBoardView, deleteImageView, imageUploadView, userProfileView

app_name = 'core'

urlpatterns = [
    path('', dashBoardView,  name='dashboard'),
    path('my-profile/', userProfileView, name='profile'),
    path('my-favicons/', imageUploadView, name='upload'),
    path('delete/<int:pk>/', deleteImageView, name='delete-favicon'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('faq/', FAQPageView.as_view(), name='faq'),
]
