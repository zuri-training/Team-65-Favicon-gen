from email.mime import image
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.views import PasswordResetView


def register(request):
    if request.user.is_authenticated:
        messages.info(
            request, "You are already Logged In! Log out to create a new account.")
        return redirect('core:dashboard')
    if request.method == 'POST':
        list(messages.get_messages(request))
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render(request, 'accounts/signup.html')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email address already exists')
                return render(request, 'accounts/signup.html')
            else:
                user = CustomUser.objects.create_user(
                    username=username, password=password1, first_name=first_name,
                    last_name=last_name, email=email
                )
                if request.FILES:
                    profile_pic = request.FILES['profile_pic']
                    user.profile_pic = profile_pic
                user.save()
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Registration Successful')
                return redirect('core:dashboard')
        else:
            messages.info(request, 'Passwords don\'t match')
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    if request.method == 'POST':
        list(messages.get_messages(request))
        username = request.POST['username']
        password1 = request.POST['password1']
        rememberMe = request.POST.get("rememberMe")
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if not rememberMe:
                request.session.set_expiry(0)
            else:
                rememberMe = "False"
            # Redirect to a success page.
            return redirect('core:dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.info(request, 'Wrong Username or Password, try again')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('core:dashboard')
    else:
        logout(request)
        messages.success(request, 'You have been logged out Succesfully')
        return redirect('accounts:login')


def view_404(request, exception=None):
    return redirect("core:dashboard")
