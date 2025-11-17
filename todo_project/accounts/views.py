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

    # passamos hide_nav=True para o template
    return render(request, "login.html", {"hide_nav": True})


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

    # passamos hide_nav=True para o template
    return render(request, "register.html", {"hide_nav": True})
