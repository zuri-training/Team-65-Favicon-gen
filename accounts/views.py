from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from core.engine import createFavicons

CustomUser.UserModel = get_user_model()


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.success(request, 'Username Taken')
                return render(request, 'accounts/signup.html')
            elif CustomUser.objects.filter(email=email).exists():
                messages.success(request, 'Email address already exists')
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
                login(request, user)
                return redirect('core:dashboard')
        else:
            messages.success(request, 'Passwords don\'t match')
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('core:dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Wrong Username or Password, try again')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('core:dashboard')
    else:
        logout(request)
        messages.success(request, 'Logged Out Succesfully')
        return redirect('accounts:login')
