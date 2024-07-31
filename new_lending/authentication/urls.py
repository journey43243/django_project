from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.Authenticate.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('regist/', views.Registration.as_view(), name='regist'),
    path('reset-password/', views.ResetPassword.as_view(), name='reset_password'),
    path('password-reset-confirm/<uidb64>/<token>', views.ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
]