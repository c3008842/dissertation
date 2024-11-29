from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.conf.urls.static import static



urlpatterns = [
    path('home', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
   
    path('base', views.base, name="base"),
    

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done1.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm1.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete1.html'), name='password_reset_complete'),

    path('change/password', login_required(PasswordChangeView.as_view(
        template_name='registration/changePassword.html',
        success_url='/password-change-done/'
    )), name='change/password'),

    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='registration/changeDone.html'
    ), name='password_change_done'),

    path('user/engagement/metrics', views.retrieveMachineData, name="user/engagement/metrics"),
    path('home/', views.healthStatus, name="home"),
    path('overall/metrics', views.overallMetrics, name="overall/metrics"),
    path('session/data', views.allSessionData, name="session/data"),
    path('change/password', views.changePassword, name="change/password"),
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)