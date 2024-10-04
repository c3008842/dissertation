from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('base', views.base, name="base"),
    path('registration', views.registrationPage, name="registration"),
    path('reset/email/', views.resetPage, name="reset/email/"),
    path('reset/message/', views.resetPasswordLink, name="reset/message/"),
    path('reset/password/', views.resetPasswordPage, name="reset/password/"),
    path('reset/success/', views.resetPasswordSuccessMessage, name="reset/success/"),
    path('graph/', views.barGraph, name="graph"),
   
]