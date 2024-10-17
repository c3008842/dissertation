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
    path('user/engagement/metrics', views.userEngagementMetrics, name="user/engagement/metrics"),
    path('health/', views.healthStatus, name="health"),
    path('overall/metrics', views.overallMetrics, name="overall/metrics"),
    path('session/data', views.allSessionData, name="session/data"),
    path('change/password', views.changePassword, name="change/password"),
    path('add/email', views.addEmail, name="add/email"),
   
   
]