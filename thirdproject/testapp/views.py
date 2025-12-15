from django.shortcuts import render

# Create your views here.


def home_view(request):
    template_name = "testapp/index.html"
    return render(request, template_name)


def about_view(request):
    template_name = "testapp/about.html"
    return render(request, template_name)


def contact_us_view(request):
    template_name = "testapp/contact_us.html"
    return render(request, template_name)


def login_view(request):
    template_name = "testapp/login.html"
    return render(request, template_name)


def registration_view(request):
    template_name = "testapp/registration.html"
    return render(request, template_name)
