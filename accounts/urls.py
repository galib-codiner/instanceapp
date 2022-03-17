from pathlib import Path
from django import views
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    path('' ,  views.home  , name="home"),
    path('register' , views.register_attempt , name="register_attempt"),
    path('accounts/login/' , views.login_attempt , name="login_attempt"),
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error"),
    
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
    
   
]
