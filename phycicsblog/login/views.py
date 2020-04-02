from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Rejestracja
from django.contrib.auth.models import User

def home(request):
    return render(request, 'login/home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Zostałeś zalogowany pomyślnie')
            return redirect('home')
        else:
            messages.warning(request, "Login albo hasło jest nieprawidłowe !!")
            return redirect('login')
    else:
        return render(request, 'login/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = Rejestracja(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Twoje konto zostało stworzone!!")
            return redirect('login')
        else:
            form = Rejestracja(request.POST)
    else:
        form = Rejestracja()
    context = {
        'form': form,
    }
    return render(request, 'login/register.html', context)
