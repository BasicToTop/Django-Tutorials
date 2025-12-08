from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    sum = 10+20  # Simple logic example
    return HttpResponse(f"<span style='color:red;'>Welcome</span><br> to the Home Page of Main App!--> {sum}")


def about_view(request):
    return HttpResponse("This is the About Page of Main App!")


def sum(request, a, b):
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is <b>{result}</b>.")
