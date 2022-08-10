from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
