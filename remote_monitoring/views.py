from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home.html')

def settings(request):
    return render(request, 'changepassword.html')

def base(request):
    return render(request, 'base.html')


def data(request):
    return render(request, 'transaction_details.html')
