from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

from .forms import LoginForm, RegistrationForm      

@login_required(login_url='signin')
def home(request):
    response = requests.get('https://api.imgflip.com/get_memes').json()
    return render(request, 'home.html',{'response':response})

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("<html><h1>please enter valid username and password </h1></html>")
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)

def signout(request):
    logout(request)
    return redirect('signin')