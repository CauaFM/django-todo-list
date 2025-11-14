from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe!")
        else:
            User.objects.create_user(username=username, password=password)
            return redirect("login")

    return render(request, "register.html")