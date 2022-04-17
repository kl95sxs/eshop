from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

def home (request):
    return render (request, 'shop/home.html')
def signupuser (request):
    if request.method == 'GET':
        return render (request, 'shop/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('currentcart')
            except IntegrityError:
                return render (request, 'shop/signupuser.html', {'form': UserCreationForm(), 'error': 'Такое имя уже используется'})


        else:
            return render (request, 'shop/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def currentcart(request):
    return render (request, 'shop/currentcart.html')
def logoutuser (request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        
