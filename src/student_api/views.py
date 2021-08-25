from django.shortcuts import render, HttpResponse

from .models import Student

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')