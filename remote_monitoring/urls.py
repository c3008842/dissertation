from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('base', views.base, name="base"),
    path('registration', views.registrationPage, name="registration"),
    path('reset/email/', views.resetPage, name="reset/email"),
    path('reset/message/', views.resetPasswordLink, name="reset/message/"),
    path('reset/password/', views.resetPasswordPage, name="reset/password/"),
    path('reset/success/', views.resetPasswordSuccessMessage, name="reset/success/"),
    path('user/engagement/metrics', views.userEngagementMetrics, name="user/engagement/metrics"),
    path('home/', views.healthStatus, name="home"),
    path('overall/metrics', views.overallMetrics, name="overall/metrics"),
    path('session/data', views.allSessionData, name="session/data"),
    path('change/password', views.changePassword, name="change/password"),
    path('add/email', views.addEmail, name="add/email"),
   
   
]