from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
import requests
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'registration/home.html')

def login(request):
    return render(request, 'registration/login.html')

def registrationPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!!!')
                return redirect('login')  # Redirect to the login page after successful registration
            else:
                messages.error(request, 'Please correct the errors below')
        except Exception as e:
            messages.error(request, f'Something went wrong: {str(e)}') # Display error message on registration page
            form = RegisterForm()
            return redirect('registration')
        
    else:
        form = RegisterForm()

    return render(request, 'registration/registrationPage.html', {'form': form})
  

def base(request):
    return render(request, 'registration/base.html')

# def resetPage(request):
#     return render(request, 'resetPage.html')

# def resetPasswordLink(request):
#     return render(request, 'resetPasswordMessage.html')

# def resetPasswordPage(request):
#     return render(request, 'resetPasswordPage.html')

# def resetPasswordSuccessMessage(request):
#     return render(request, 'resetPasswordSuccessMessage.html')

def userEngagementMetrics(request):
    return render(request, 'registration/userEngagementMetrics.html')

def healthStatus(request):
    return render(request, 'registration/health_dashboard.html')

def overallMetrics(request):
    return render(request, 'registration/overall_metrics.html')


def allSessionData(request):
    return render(request, 'registration/allSessionData.html')


def changePassword(request):
    return render(request, 'registration/changePassword.html')


def addEmail(request):
    return render(request, 'registration/addEmail.html')







