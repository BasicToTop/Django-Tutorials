from django.shortcuts import render, redirect
from mainapp.forms import UserRegistration, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_registration(request):
    if request.method == 'GET':
        form = UserRegistration()
        template_name = 'mainapp/user_registration.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            template_name = 'mainapp/user_registration.html'
            context = {'form': form}
            return render(request, template_name, context)


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        template_name = 'mainapp/login.html'
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print('username:', username)
            print('password:', password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # then user is authenticated successfully
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid username or password.")

                template_name = 'mainapp/login.html'
                context = {'form': form}
                return render(request, template_name, context)

        else:
            template_name = 'mainapp/login.html'
            context = {'form': form}
            return render(request, template_name, context)


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    template_name = 'mainapp/dashboard.html'
    context = {}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect('login')


def about_view(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('login')
    template_name = 'mainapp/about.html'
    context = {}
    return render(request, template_name, context)