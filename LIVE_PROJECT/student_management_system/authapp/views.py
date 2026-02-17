from django.shortcuts import redirect, render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
# Create your views here.


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        template_name = 'authapp/login.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {'form': form, 'error': 'Invalid credentials'}
                return render(request, 'authapp/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authapp/login.html', context)
        # will handle the login logic here in future


def user_registration_view(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        template_name = 'authapp/register.html'
        context = {'form': form}
        return render(request, template_name, context)
        # will handle the registration logic here in future
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            obj = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=make_password(password)
            )
            obj.save()
            # form.save()
            # will handle the registration logic here in future
            return redirect('login')
        else:
            template_name = 'authapp/register.html'
            context = {'form': form}
            return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')
