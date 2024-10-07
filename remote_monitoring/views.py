from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registrationPage(request):
    return render(request, 'registrationPage.html')

def base(request):
    return render(request, 'base.html')

def resetPage(request):
    return render(request, 'resetPage.html')

def resetPasswordLink(request):
    return render(request, 'resetPasswordMessage.html')

def resetPasswordPage(request):
    return render(request, 'resetPasswordPage.html')

def resetPasswordSuccessMessage(request):
    return render(request, 'resetPasswordSuccessMessage.html')

def barGraph(request):
    return render(request, 'bargraph.html')

def healthStatus(request):
    return render(request, 'overview.html')
