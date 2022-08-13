from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='accounts/pass1.html', success_url=reverse_lazy('accounts:password_reset_done')),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/pass2.html'),
         name='password_reset_done'),

    path('password_change/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/pass3.html', success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
