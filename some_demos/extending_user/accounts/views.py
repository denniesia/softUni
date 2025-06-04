from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from .forms import  CustomUserCreationForm
# Create your views here.

class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

class RegisterUserView(views.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')