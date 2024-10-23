from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('home', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('base', views.base, name="base"),
    path('registration', views.registrationPage, name="registration"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done_page.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm_page.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_page.html'), name='password_reset_complete'),

    path('user/engagement/metrics', views.userEngagementMetrics, name="user/engagement/metrics"),
    path('home/', views.healthStatus, name="home"),
    path('overall/metrics', views.overallMetrics, name="overall/metrics"),
    path('session/data', views.allSessionData, name="session/data"),
    path('add/email', views.addEmail, name="add/email"),
  

   
]