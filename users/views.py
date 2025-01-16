from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users\siginup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'users\login.html'

class UserLogoutView(LogoutView):
    template_name = 'users\login.html'

class UserProfileView(TemplateView):
    template_name = 'users\profile.html'