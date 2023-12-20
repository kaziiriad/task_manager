from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:

            if User.objects.filter(username=username).exists():

                messages.info(request, "Username already taken!")
                return redirect('register')

            elif User.objects.filter(email=email).exists():

                messages.info(request, "Email already taken!")
                return redirect('register')

            else:
                
                user = User.objects.create(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                messages.success(request, 'Registration Successful!')
                return redirect('login')

        else:
            messages.info(request, "Passwords are not matching!")
            return redirect('register')


    return render(request, 'accounts/register.html')


def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout_user(request):

    logout(request)

    return redirect('home')