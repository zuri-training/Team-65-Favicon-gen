from django.urls import path
from .views import AboutPageView, FAQPageView, HowItWorksPageView, PrivacyPolicyPageView, contactPageView, dashBoardView, deleteImageView, imageUploadView, userProfileView

app_name = 'core'

urlpatterns = [
    path('', dashBoardView,  name='dashboard'),
    path('my-profile/', userProfileView, name='profile'),
    path('my-favicons/', imageUploadView, name='upload'),
    path('delete/<int:pk>/', deleteImageView, name='delete-favicon'),
    path('contact/', contactPageView, name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('how-it-works/', HowItWorksPageView.as_view(), name='how-it-works'),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy-policy'),
]
