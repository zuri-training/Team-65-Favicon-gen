from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(),
     name='reset_password'),
    
    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),
    
    path('password_change/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
    
    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete'),
]
# template_name='password1.html'