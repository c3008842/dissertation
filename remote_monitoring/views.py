from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'setting.html')
