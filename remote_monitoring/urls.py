from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('settings', views.settings, name="settings"),
    path('base', views.base, name="base"),
    path('data', views.data, name="data"),
   
]