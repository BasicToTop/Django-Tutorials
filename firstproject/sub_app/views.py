from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def multiply(request, a, b):
    result = a*b
    return HttpResponse(f'<h1>mul of {a} and {b}: {result} </h1>')
